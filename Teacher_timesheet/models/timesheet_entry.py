from odoo import models, fields, api

class TimesheetEntry(models.Model):
    _name = 'class.timesheet.entry'
    _description = 'Teacher Timesheet Entry'

    teacher_id = fields.Many2one(
        'res.partner',
        string="Teacher",
        required=True,
        domain="[('is_teacher', '=', True)]"
    )
    class_name = fields.Char(string="Class Name", required=True)
    start_time = fields.Datetime(string="Start Time", required=True)
    end_time = fields.Datetime(string="End Time", required=True)
    duration = fields.Float(
        string="Duration (Hours)",
        compute="_compute_duration",
        store=True,
        readonly=True
    )
    class_payroll_status = fields.Selection([
        ('upcoming', 'Upcoming Class'),
        ('success', 'Successfully Taught (Hours Added)'),
        ('cancelled', 'Cancelled Class (No Hours)'),
    ], string="Payroll Status", default='upcoming', required=True)

    @api.depends('start_time', 'end_time')
    def _compute_duration(self):
        for record in self:
            if record.start_time and record.end_time:
                delta = record.end_time - record.start_time
                record.duration = delta.total_seconds() / 3600.0
            else:
                record.duration = 0.0
