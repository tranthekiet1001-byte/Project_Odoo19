{
    'name': 'Work Planned',
    'version': '19.0.1.0.0',
    'category': 'Human Resources/Attendances',
    'sequence': 241,
    'summary': 'Track approved work schedules and planned work shifts',
    'description': """
This module aims to manage approved work schedules for employees.
==================================================================

Allows teachers/employees to view their approved work shifts and schedules.
Only approved shifts will be recognized when checking in/out.

Features:
- View approved work schedules by employee
- Filter by date range, department
- List view of planned work shifts
- Integration with hr.attendance for attendance tracking
    """,
    'website': 'https://www.odoo.com/app/attendances',
    'author': 'Your Company',
    'license': 'LGPL-3',
    'depends': ['hr', 'hr_attendance', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_work_planned_view.xml',
        'views/hr_employee_view.xml',
    ],
    'installable': True,
    'application': True,
}
