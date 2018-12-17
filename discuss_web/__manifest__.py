# -*- coding: utf-8 -*-
{
    'name': "discuss_web",

    'summary': """
        Discuss to backend
        """,

    'description': """
        Discuss to frontend as part of website
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/10.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'website_mail', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        #'vievs/website_data.xml',
        'views/website_discuss_templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}