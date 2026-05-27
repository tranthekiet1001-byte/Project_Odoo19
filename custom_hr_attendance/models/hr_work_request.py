# -*- coding: utf-8 -*-
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError, UserError
from datetime import timedelta


class HrWorkRequest(models.Model):
    _name = 'hr.work.request'
    _description = 'Đơn làm việc Online / Công tác'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'date_from desc, id desc'

    # -------------------------------------------------------------------------
    # Định danh
    # -------------------------------------------------------------------------
    name = fields.Char(
        string='Mã đơn',
        readonly=True,
        default='New',
        copy=False,
        tracking=True,
    )

    # -------------------------------------------------------------------------
    # Thông tin nhân viên
    # -------------------------------------------------------------------------
    employee_id = fields.Many2one(
        'hr.employee',
        string='Nhân viên',
        required=True,
        default=lambda self: self.env.user.employee_id,
        tracking=True,
    )
    department_id = fields.Many2one(
        'hr.department',
        string='Phòng ban',
        related='employee_id.department_id',
        store=True,
        readonly=True,
    )
    manager_id = fields.Many2one(
        'hr.employee',
        string='Quản lý trực tiếp',
        related='employee_id.parent_id',
        store=True,
        readonly=True,
        tracking=True,
    )
    company_id = fields.Many2one(
        'res.company',
        string='Công ty',
        related='employee_id.company_id',
        store=True,
        readonly=True,
    )

    # -------------------------------------------------------------------------
    # Loại đơn (SELECTION — trọng tâm yêu cầu)
    # -------------------------------------------------------------------------
    request_type = fields.Selection(
        selection=[
            ('online', 'Làm việc Online (WFH)'),
            ('business_trip', 'Công tác'),
        ],
        string='Loại đơn',
        required=True,
        default='online',
        tracking=True,
    )

    # -------------------------------------------------------------------------
    # Thời gian
    # -------------------------------------------------------------------------
    date_from = fields.Datetime(
        string='Từ ngày / giờ',
        required=True,
        tracking=True,
        default=fields.Datetime.now,
    )
    date_to = fields.Datetime(
        string='Đến ngày / giờ',
        required=True,
        tracking=True,
    )
    number_of_days = fields.Float(
        string='Số ngày',
        compute='_compute_number_of_days',
        store=True,
        readonly=True,
    )

    # -------------------------------------------------------------------------
    # Nội dung đơn
    # -------------------------------------------------------------------------
    work_location = fields.Char(
        string='Địa điểm làm việc / Công tác',
        help='Địa chỉ làm việc online hoặc địa điểm công tác',
    )
    reason = fields.Text(
        string='Lý do / Mục đích',
        required=True,
        tracking=True,
    )
    task_description = fields.Text(
        string='Công việc dự kiến',
        help='Mô tả các công việc sẽ thực hiện trong thời gian này',
    )
    attachment_ids = fields.Many2many(
        'ir.attachment',
        string='Tài liệu đính kèm',
        help='Giấy mời công tác, kế hoạch, hoặc tài liệu liên quan',
    )

    # -------------------------------------------------------------------------
    # Dành cho công tác
    # -------------------------------------------------------------------------
    destination = fields.Char(
        string='Điểm đến công tác',
    )
    transport_mode = fields.Selection(
        selection=[
            ('personal', 'Phương tiện cá nhân'),
            ('company', 'Phương tiện công ty'),
            ('public', 'Phương tiện công cộng'),
            ('flight', 'Máy bay'),
        ],
        string='Phương tiện di chuyển',
    )
    estimated_cost = fields.Float(
        string='Chi phí dự kiến (VNĐ)',
        digits=(15, 0),
    )
    currency_id = fields.Many2one(
        'res.currency',
        string='Tiền tệ',
        related='company_id.currency_id',
        readonly=True,
        store=False,
    )

    # -------------------------------------------------------------------------
    # Trạng thái & phê duyệt
    # -------------------------------------------------------------------------
    state = fields.Selection(
        selection=[
            ('draft', 'Nháp'),
            ('confirm', 'Chờ duyệt'),
            ('validate', 'Đã duyệt'),
            ('refuse', 'Từ chối'),
        ],
        string='Trạng thái',
        default='draft',
        required=True,
        tracking=True,
        copy=False,
    )
    validated_by = fields.Many2one(
        'res.users',
        string='Người duyệt',
        readonly=True,
        copy=False,
        tracking=True,
    )
    validation_date = fields.Datetime(
        string='Ngày duyệt',
        readonly=True,
        copy=False,
    )
    refuse_reason = fields.Text(
        string='Lý do từ chối',
        copy=False,
        tracking=True,
    )

    # =========================================================================
    # COMPUTE
    # =========================================================================

    @api.depends('date_from', 'date_to')
    def _compute_number_of_days(self):
        for rec in self:
            if rec.date_from and rec.date_to:
                delta = rec.date_to - rec.date_from
                # Tính theo giờ làm việc: 8h/ngày
                rec.number_of_days = round(delta.total_seconds() / 3600 / 8, 1)
            else:
                rec.number_of_days = 0.0

    # =========================================================================
    # CONSTRAINTS
    # =========================================================================

    @api.constrains('date_from', 'date_to')
    def _check_dates(self):
        for rec in self:
            if rec.date_from and rec.date_to:
                if rec.date_to <= rec.date_from:
                    raise ValidationError(
                        _('Ngày kết thúc phải sau ngày bắt đầu.')
                    )
                # Kiểm tra trùng đơn cùng nhân viên
                domain = [
                    ('employee_id', '=', rec.employee_id.id),
                    ('state', 'not in', ['refuse']),
                    ('id', '!=', rec.id),
                    ('date_from', '<', rec.date_to),
                    ('date_to', '>', rec.date_from),
                ]
                overlap = self.search(domain, limit=1)
                if overlap:
                    raise ValidationError(_(
                        'Nhân viên %(name)s đã có đơn %(req)s trùng thời gian này.',
                        name=rec.employee_id.name,
                        req=overlap.name,
                    ))

    @api.constrains('request_type', 'destination')
    def _check_business_trip_destination(self):
        for rec in self:
            if rec.request_type == 'business_trip' and not rec.destination:
                raise ValidationError(
                    _('Vui lòng nhập điểm đến cho đơn Công tác.')
                )

    # =========================================================================
    # ONCHANGE
    # =========================================================================

    @api.onchange('request_type')
    def _onchange_request_type(self):
        """Xóa các field không liên quan khi đổi loại đơn"""
        if self.request_type == 'online':
            self.destination = False
            self.transport_mode = False
            self.estimated_cost = 0.0
        elif self.request_type == 'business_trip':
            self.work_location = False

    @api.onchange('date_from')
    def _onchange_date_from(self):
        """Tự điền date_to = date_from + 1 ngày làm việc"""
        if self.date_from and not self.date_to:
            self.date_to = self.date_from + timedelta(hours=8)

    # =========================================================================
    # ACTIONS / WORKFLOW
    # =========================================================================

    def action_confirm(self):
        """Gửi đơn chờ duyệt"""
        for rec in self:
            if rec.state != 'draft':
                raise UserError(_('Chỉ có thể gửi đơn ở trạng thái Nháp.'))
            rec.write({'state': 'confirm'})
            # Gửi thông báo cho quản lý
            if rec.manager_id and rec.manager_id.user_id:
                rec.activity_schedule(
                    'mail.mail_activity_data_todo',
                    summary=_('Đơn %(type)s cần duyệt từ %(name)s', 
                              type=dict(rec._fields['request_type'].selection).get(rec.request_type),
                              name=rec.employee_id.name),
                    user_id=rec.manager_id.user_id.id,
                    date_deadline=fields.Date.today() + timedelta(days=1),
                )
        return True

    def action_validate(self):
        """Phê duyệt đơn"""
        for rec in self:
            if rec.state != 'confirm':
                raise UserError(_('Chỉ có thể duyệt đơn đang ở trạng thái Chờ duyệt.'))
            rec.write({
                'state': 'validate',
                'validated_by': self.env.user.id,
                'validation_date': fields.Datetime.now(),
            })
            rec.activity_feedback(['mail.mail_activity_data_todo'])
            # Thông báo kết quả cho nhân viên
            rec.message_post(
                body=_('✅ Đơn đã được phê duyệt bởi %s', self.env.user.name),
                message_type='notification',
                subtype_xmlid='mail.mt_comment',
            )
        return True

    def action_refuse(self):
        """Từ chối đơn — mở wizard nhập lý do"""
        return {
            'type': 'ir.actions.act_window',
            'name': _('Lý do từ chối'),
            'res_model': 'hr.work.request.refuse.wizard',
            'view_mode': 'form',
            'target': 'new',
            'context': {'default_request_id': self.id},
        }

    def action_reset_draft(self):
        """Đặt lại về Nháp"""
        for rec in self:
            if rec.state not in ('confirm', 'refuse'):
                raise UserError(_('Chỉ có thể đặt lại đơn từ trạng thái Chờ duyệt hoặc Từ chối.'))
            rec.write({
                'state': 'draft',
                'refuse_reason': False,
                'validated_by': False,
                'validation_date': False,
            })
        return True

    # =========================================================================
    # HELPER — dùng cho smart button trên Employee form
    # =========================================================================

    @api.model
    def action_open_work_requests(self):
        """Không dùng trực tiếp — xem hr_employee.py"""
        pass

    # =========================================================================
    # ORM OVERRIDES
    # =========================================================================

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('hr.work.request') or 'New'
        return super().create(vals_list)

    def unlink(self):
        for rec in self:
            if rec.state not in ('draft', 'refuse'):
                raise UserError(
                    _('Không thể xóa đơn đang ở trạng thái "%s". Vui lòng từ chối trước.', rec.state)
                )
        return super().unlink()


# =============================================================================
# WIZARD: Từ chối đơn
# =============================================================================

class HrWorkRequestRefuseWizard(models.TransientModel):
    _name = 'hr.work.request.refuse.wizard'
    _description = 'Wizard Từ chối đơn làm việc'

    request_id = fields.Many2one(
        'hr.work.request',
        string='Đơn',
        required=True,
    )
    refuse_reason = fields.Text(
        string='Lý do từ chối',
        required=True,
    )

    def action_refuse_confirm(self):
        self.request_id.write({
            'state': 'refuse',
            'refuse_reason': self.refuse_reason,
        })
        self.request_id.message_post(
            body=_('❌ Đơn bị từ chối. Lý do: %s', self.refuse_reason),
            message_type='notification',
            subtype_xmlid='mail.mt_comment',
        )
        self.request_id.activity_feedback(['mail.mail_activity_data_todo'])
        return {'type': 'ir.actions.act_window_close'}
