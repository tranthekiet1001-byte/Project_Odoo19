# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    work_planned_ids = fields.One2many(
        'hr.work.planned',
        'employee_id',
        string='Planned Work Schedules',
        help="List of approved work schedules"
    )

    planned_hours = fields.Float(
        string='Total Planned Hours',
        compute='_compute_planned_hours',
        store=True,
        readonly=True,
        help="Total approved planned hours of this employee"
    )

    @api.depends('work_planned_ids.planned_hours', 'work_planned_ids.status')
    def _compute_planned_hours(self):
        for employee in self:
            approved_plans = employee.work_planned_ids.filtered(
                lambda plan: plan.status == 'approved'
            )
            employee.planned_hours = sum(approved_plans.mapped('planned_hours'))
