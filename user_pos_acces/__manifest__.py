# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) Falcon Solutions SpA
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': "Access POS MFH",
    'summary': """user_pos_acces""",
    'description': """
        Restricts user access to points of sale.
    """,
    'author': "Falcon Solutions SpA",
    'maintainer': 'Falcon Solutions',
    'website': 'http://www.falconsolutions.cl',
    'license': 'AGPL-3',
    'category': "Point of Sale",
    'version': '10.0.1',
    'depends': [ 
                'point_of_sale',
                ],
    'data': [
        'views/pos_config_view.xml',
        'data/rules.xml',
    ],
    'demo': [
    ],
    'images': ['static/description/banner.jpg'],
    "license": 'AGPL-3',
    'installable': True,
}
