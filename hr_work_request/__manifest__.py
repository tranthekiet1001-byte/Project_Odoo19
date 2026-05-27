# -*- coding: utf-8 -*-
{
    'name': 'HR Work Request (Online / Công tác)',
    'version': '18.0.1.0.0',
    'summary': 'Quản lý đơn làm việc Online (WFH) và Công tác',
    'description': """
        Mở rộng module hr_attendance:
        - Tạo đơn làm việc Online (WFH) hoặc Công tác
        - Quy trình duyệt: Nháp → Chờ duyệt → Duyệt / Từ chối
        - Tab riêng trong hồ sơ nhân viên
        - Menu quản lý đơn trong Attendances
    """,
    'category': 'Human Resources/Attendances',
    'author': 'Custom Dev',
    'depends': [
        'hr',
        'mail',
        'hr_attendance',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence_data.xml',
        'views/hr_work_request_views.xml',
        'views/hr_employee_views_inherit.xml',
        'views/menu_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
