{
    'name': 'Multiuser To-Do',
    'description': 'Extend the To-Do app to multiuser.',
    'author': 'Santoni',
    'description': """
This module allows users to create their own notes inside Odoo
=================================================================


""",
    'depends': ['todo_app'],
    'application': True,
    'data': [
        # 'security/ir.model.access.csv',
        # 'security/todo_access_rules.xml',
        # 'views/todo_menu.xml',
        'views/todo_task.xml'
    ],
}
