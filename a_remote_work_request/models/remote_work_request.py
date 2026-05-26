from odoo import fields, models


class RemoteWorkRequest(models.Model):
    _name = "a.remote.work.request"
    _description = "Remote Work Request"
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
            ("event", "Đi sự kiện bên ngoài"),
            ("partner", "Đi gặp đối tác ở bên ngoài"),
            ("other", "Khác (Theo yêu cầu của BGĐ)"),
            ("home", "Work from home"),
        ],
        string="Work Type",
        required=True,
        default="home",
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
