# -*- coding: utf-8 -*-
{
    'name': "custom_site",
    'summary': """
        custom_site widget
        """,
    'description': """
        custom widget
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['website'],

    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'demo': [
        'data/demo.xml',
    ],
    'application': True,
}