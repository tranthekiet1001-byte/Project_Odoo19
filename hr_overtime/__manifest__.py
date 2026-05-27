{
    'name': 'Overtime Management',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Manage employee overtime requests and integrate with timesheets',
    'description': """
        Overtime Management Module
        ==========================
        - Create and manage overtime requests
        - Approval workflow for managers
        - Auto-calculate overtime hours
        - Automatically generate timesheet records upon approval
    """,
    'author': 'Antigravity',
    'depends': ['base', 'hr', 'hr_timesheet'],
    'data': [
        'security/hr_overtime_security.xml',
        'security/ir.model.access.csv',
        'views/hr_overtime_views.xml',
        'views/hr_overtime_menus.xml',
    ],
    'demo': [
        'demo/hr_overtime_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
