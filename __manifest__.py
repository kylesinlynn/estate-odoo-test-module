# -*- coding: utf-8 -*-
{
    'name': "Real Estate",

    'summary': """
        Estate Agent for House buying and selling""",

    'description': """
        Providing the best of house buying and selling
    """,

    'author': "Kyle Sin Lynn",
    'website': "http://kylesinlynn.ml",
    
    'category': 'Housing',
    'version': '0.01',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/menus.xml',
        'views/property_views.xml',
        'views/type_views.xml',
        'views/tag_views.xml',
    ],
    
    'installable': True,
}
