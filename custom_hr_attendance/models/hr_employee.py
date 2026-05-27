# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    work_request_ids = fields.One2many(
        'hr.work.request',
        'employee_id',
        string='Đơn làm việc',
    )

    work_request_count = fields.Integer(
        string='Số đơn làm việc',
        compute='_compute_work_request_count',
    )

    @api.depends('work_request_ids')
    def _compute_work_request_count(self):
        for emp in self:
            emp.work_request_count = len(emp.work_request_ids)

    def action_open_work_requests(self):
        """Smart button: mở danh sách đơn làm việc của nhân viên"""
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': _('Đơn làm việc — %s', self.name),
            'res_model': 'hr.work.request',
            'view_mode': 'list,form',
            'domain': [('employee_id', '=', self.id)],
            'context': {
                'default_employee_id': self.id,
                'search_default_employee_id': self.id,
            },
        }
