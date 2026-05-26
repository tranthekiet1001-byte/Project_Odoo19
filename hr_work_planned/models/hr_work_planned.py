# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class HrWorkPlanned(models.Model):
    _name = 'hr.work.planned'
    _description = "Work Planned Schedule"
    _order = "date_start desc, employee_id"
    _inherit = ["mail.thread"]

    def _default_employee(self):
        """Return default employee (current user's employee)"""
        if self.env.user.has_group('hr_attendance.group_hr_attendance_user'):
            return self.env.user.employee_id.id
        return None

    employee_id = fields.Many2one(
        'hr.employee', 
        string="Employee", 
        default=lambda self: self._default_employee(), 
        required=True,
        ondelete='cascade', 
        index=True
    )
    department_id = fields.Many2one(
        'hr.department', 
        string="Department", 
        related="employee_id.department_id",
        readonly=True,
        store=True
    )
    manager_id = fields.Many2one(
        comodel_name='hr.employee', 
        related="employee_id.parent_id", 
        readonly=True,
        store=True
    )
    date_start = fields.Datetime(
        string="Scheduled Start Time", 
        required=True, 
        tracking=True, 
        index=True
    )
    date_end = fields.Datetime(
        string="Scheduled End Time", 
        required=True, 
        tracking=True
    )
    date = fields.Date(
        string="Date", 
        compute='_compute_date', 
        store=True, 
        index=True
    )
    planned_hours = fields.Float(
        string='Planned Hours', 
        compute='_compute_planned_hours', 
        store=True, 
        readonly=True
    )
    status = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('approved', 'Approved'),
            ('rejected', 'Rejected'),
        ],
        string='Status',
        default='draft',
        tracking=True,
        index=True
    )
    description = fields.Text(
        string='Description/Notes',
        help="Additional notes about this planned work shift"
    )
    is_manager = fields.Boolean(compute="_compute_is_manager")
    color = fields.Integer(compute='_compute_color')

    @api.depends('date_start')
    def _compute_date(self):
        """Compute the date from date_start"""
        for record in self:
            if record.date_start:
                record.date = record.date_start.date()
            else:
                record.date = False

    @api.depends('date_start', 'date_end')
    def _compute_planned_hours(self):
        """Compute planned hours from start and end time"""
        for record in self:
            if record.date_start and record.date_end:
                delta = record.date_end - record.date_start
                record.planned_hours = delta.total_seconds() / 3600.0
            else:
                record.planned_hours = 0.0

    @api.depends('employee_id')
    def _compute_is_manager(self):
        """Check if current user is manager of the employee"""
        for record in self:
            manager = record.employee_id.parent_id
            record.is_manager = manager and manager.user_id and manager.user_id == self.env.user

    @api.depends('status')
    def _compute_color(self):
        """Compute color based on status"""
        for record in self:
            if record.status == 'approved':
                record.color = 10  # green
            elif record.status == 'rejected':
                record.color = 1   # red
            else:
                record.color = 0   # default

    def action_approve(self):
        """Action to approve the work planned"""
        self.write({'status': 'approved'})
        return True

    def action_reject(self):
        """Action to reject the work planned"""
        self.write({'status': 'rejected'})
        return True

    def action_reset_to_draft(self):
        """Action to reset status to draft"""
        self.write({'status': 'draft'})
        return True
