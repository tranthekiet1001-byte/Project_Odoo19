{
    "name": "Remote Work Request",
    "version": "1.0",
    "category": "Human Resources",
    "author": "Nguyễn Hồ Thanh My",
    "summary": "Manage remote work requests",
    "depends": ["base", "hr"],
    "data": [
        "security/ir.model.access.csv",
        "views/remote_work_request_views.xml",
        "views/remote_work_request_menu.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "a_remote_work_request/static/src/scss/remote_work_request.scss",
        ],
    },
    "installable": True,
    "application": True,
    "license": "LGPL-3",
}
