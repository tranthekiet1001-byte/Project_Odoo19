{
    "name": "Attendances Time Adjustment",
    "version": "1.0",
    "category": "Human Resources",
    "author": "Nguyễn Hồ Thanh My",
    "summary": "Manage attendance time adjustment requests by Teppi",
    "depends": ["base", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/time_adjustment_views.xml",
        "views/time_adjustment_menu.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "hr_attendances_time_adjustment/static/src/scss/time_adjustment.scss",
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
