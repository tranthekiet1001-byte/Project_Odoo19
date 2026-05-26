{
    'name': 'HR Work Schedule',
    'version': '1.0',
    'category': 'Human Resources',
    'summary': 'Quản lý công ca theo Kanban',
    'description': 'Module quản lý công ca của giáo viên, có trạng thái Draft, Submitted, Approved, Reject.',
    'author': 'Châu',
    'depends': ['hr_attendance'],
    'data': [
        'security/ir.model.access.csv',
        'views/hr_work_schedule_views.xml',
    ],
    'installable': True,
    'application': True,
}
