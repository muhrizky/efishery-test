{
    'name': 'Fetch Module',
    'version': '1.0.0',
    'category': 'Tools',
    'author': 'Muhammad Rizqi',
    'license': 'AGPL-3',
    'summary': 'Fetch data, add USD price, and enforce role-based access control',
    'description': '',
    'depends': [
        'base', 'auth_module'
    ],
    'data': [
        'security/ir.model.access.csv',
        "views/views.xml",
        "views/fish_price.xml",
    ],
    'installable': True,
    'auto_install': False,
}
