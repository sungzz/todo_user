{
    'name': 'Multiuser To-Do',
    'description': 'Extend the To-Do app to multiuser.',
    'author': 'Santoni',
    'description': """
This module allows users to create their own notes inside Odoo
=================================================================


""",
    'depends': ['todo_app','mail'],
    'application': True,
    'data': [
        'views/todo_task.xml',
        'security/todo_access_rules.xml'
    ],
}
