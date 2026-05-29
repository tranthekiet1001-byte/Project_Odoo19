{
    'name': 'Teacher Timesheet',
    'version': '18.0.1.0.0',
    'summary': 'Manual entry of teachers teaching hours for payroll purposes.',
    'category': 'Human Resources',
    'author': 'Ngoc Han',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/timesheet_views.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}
