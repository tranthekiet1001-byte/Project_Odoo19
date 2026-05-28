from odoo import fields, models


class AttendanceTimeAdjustment(models.Model):
    _name = "hr.attendance.time.adjustment"
    _description = "Attendance Time Adjustment"
    _order = "id desc"
    _rec_name = "name"

    name = fields.Char(string="Request Name", required=True, copy=False, default="New")
    employee_id = fields.Many2one("hr.employee", string="Employee", required=True)
    manager_id = fields.Many2one("hr.employee", string="Manager")
    department_id = fields.Many2one("hr.department", string="Department")
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.company,
        required=True,
    )
    work_type = fields.Selection(
        [
            ("check_in", "Check In"),
            ("check_out", "Check Out"),
        ],
        string="Work Type",
        required=True,
        default="check_in",
    )
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    description = fields.Text(string="Description")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("submitted", "Submitted"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        string="Status",
        default="draft",
        required=True,
    )

    def action_submit_time_adjustment(self):
        for record in self:
            record.state = "submitted"

    def action_approve_time_adjustment(self):
        for record in self:
            record.state = "approved"

    def action_reject_time_adjustment(self):
        for record in self:
            record.state = "rejected"


class RemoteWorkRequestCompatibility(models.Model):
    _name = "a.remote.work.request"
    _description = "Remote Work Request Compatibility"
    _order = "id desc"
    _rec_name = "name"

    name = fields.Char(string="Request Name", required=True, copy=False, default="New")
    employee_id = fields.Many2one("hr.employee", string="Employee", required=True)
    manager_id = fields.Many2one("hr.employee", string="Manager")
    department_id = fields.Many2one("hr.department", string="Department")
    company_id = fields.Many2one(
        "res.company",
        string="Company",
        default=lambda self: self.env.company,
        required=True,
    )
    work_type = fields.Selection(
        [
            ("check_in", "Check In"),
            ("check_out", "Check Out"),
        ],
        string="Work Type",
        required=True,
        default="check_in",
    )
    start_date = fields.Date(string="Start Date", required=True)
    end_date = fields.Date(string="End Date", required=True)
    description = fields.Text(string="Description")
    state = fields.Selection(
        [
            ("draft", "Draft"),
            ("submitted", "Submitted"),
            ("approved", "Approved"),
            ("rejected", "Rejected"),
        ],
        string="Status",
        default="draft",
        required=True,
    )

    def action_submit(self):
        for record in self:
            record.state = "submitted"

    def action_approve(self):
        for record in self:
            record.state = "approved"

    def action_reject(self):
        for record in self:
            record.state = "rejected"
