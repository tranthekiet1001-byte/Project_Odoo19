from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class HrOvertime(models.Model):
    _name = 'hr.overtime'
    _description = 'Overtime Request'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, default=lambda self: self.env.user.employee_id)
    manager_id = fields.Many2one('hr.employee', string='Manager Approver', related='employee_id.parent_id', store=True)
    # Make department editable on the overtime record instead of a related stored field
    department_id = fields.Many2one('hr.department', string='Department')
    project_id = fields.Many2one('project.project', string='Project', help="Project for timesheet integration")
    date_start = fields.Datetime(string='Start Datetime', required=True, tracking=True)
    date_end = fields.Datetime(string='End Datetime', required=True, tracking=True)
    total_hours = fields.Float(string='Total Hours', compute='_compute_total_hours', store=True, tracking=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('submitted', 'Submitted'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected')
    ], string='Status', default='draft', tracking=True)
    note = fields.Text(string='Note/Reason')
    timesheet_id = fields.Many2one('account.analytic.line', string='Timesheet Line', readonly=True, copy=False)

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('hr.overtime') or _('New')
        return super().create(vals_list)

    @api.depends('date_start', 'date_end')
    def _compute_total_hours(self):
        for record in self:
            if record.date_start and record.date_end:
                if record.date_end < record.date_start:
                    raise ValidationError(_("End datetime cannot be earlier than start datetime."))
                delta = record.date_end - record.date_start
                record.total_hours = delta.total_seconds() / 3600.0
            else:
                record.total_hours = 0.0

    def action_submit(self):
        self.write({'state': 'submitted'})

    def action_approve(self):
        for record in self:
            if not record.project_id:
                raise ValidationError(_("Please select a Project to generate a timesheet record."))
            
            # Create timesheet record
            timesheet_vals = {
                'name': record.note or f"Overtime: {record.name}",
                'project_id': record.project_id.id,
                'employee_id': record.employee_id.id,
                'date': record.date_start.date(),
                'unit_amount': record.total_hours,
            }
            timesheet = self.env['account.analytic.line'].sudo().create(timesheet_vals)
            record.write({
                'state': 'approved',
                'timesheet_id': timesheet.id
            })

    def action_reject(self):
        self.write({'state': 'rejected'})

    def action_draft(self):
        self.write({'state': 'draft'})

    def unlink(self):
        for record in self:
            if record.state != 'draft':
                raise ValidationError(_("You can only delete overtime requests in draft state."))
            if record.timesheet_id:
                record.timesheet_id.sudo().unlink()
        return super().unlink()

    @api.onchange('employee_id')
    def _onchange_employee(self):
        for rec in self:
            if rec.employee_id:
                rec.department_id = rec.employee_id.department_id
                # manager_id is a related field, it will update automatically from employee
