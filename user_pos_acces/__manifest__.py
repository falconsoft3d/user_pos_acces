# -*- coding: utf-8 -*-
##############################################################################
#
#    ODOO, Open Source Management Solution
#    Copyright (C) 2016 Steigend IT Solutions
#    For more details, check COPYRIGHT and LICENSE files
#
##############################################################################
{
    'name': "Accesos a Puntos de Ventas",
    'summary': """user_pos_acces""",
    'description': """
        Restringe el acceso de los usuarios a los puntos de ventas.
    """,
    'author': "Falcón Solutions",
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
    "license": 'AGPL-3',
    'installable': True,
}
