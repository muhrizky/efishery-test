{
    'name': 'Auth Module',
    'version': '1.0.0',
    'category': 'Authentication',
    'author': 'Muhammad Rizqi',
    'license': 'AGPL-3',
    'summary': 'Provides a login endpoint with JWT authentication',
    'description': """
This module adds JWT-based authentication to Odoo, with features to ensure single-device login.

Features:

- **Login Endpoint (/auth_jwt/login)**: Authenticates users using email and password, returning a JWT token. Ensures users can only be logged in from one device at a time.

- **Logout Endpoint (/auth_jwt/logout)**: Invalidates the JWT token to log out the user.

Dependencies:

- **Odoo base and web modules**

- **PyJWT**: External Python library for handling JWT.

This module enhances Odoo's security by integrating JWT for user authentication.
    """,
    'depends': [
        'base',
        'web'
    ],
    'data': [
    ],
    'installable': True,
    'auto_install': False,
    'external_dependencies': {
        'python': [
            'PyJWT'
        ],
    }
}