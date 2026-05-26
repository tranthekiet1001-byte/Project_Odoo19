from odoo import models, fields, api

class HrWorkSchedule(models.Model):
    _name = 'hr.work.schedule'
    _description = 'Work Schedule'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Tên công ca", required=True)
    employee_id = fields.Many2one('hr.employee', string="Giáo viên/Người dùng", required=True)
    start_date = fields.Date(string="Ngày bắt đầu", required=True)
    end_date = fields.Date(string="Ngày kết thúc", required=True)
    # Thêm trường công ty để lọc chi nhánh
    company_id = fields.Many2one('res.company', string='Công ty', default=lambda self: self.env.company)
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('reject', 'Reject'),
    ], string="Trạng thái", default='draft', tracking=True)

    # ĐIỀU KIỆN 1: Tự động chuyển sang Submitted khi nhấn Save (Create)
    @api.model
    def create(self, vals):
        if vals.get('state') == 'draft':
            vals['state'] = 'submitted'
        return super(HrWorkSchedule, self).create(vals)

    # Các hàm nút bấm giữ nguyên
    def action_submit(self):
        self.write({'state': 'submitted'})

    def action_approve(self):
        self.write({'state': 'approved'})

    def action_reject(self):
        self.write({'state': 'reject'})