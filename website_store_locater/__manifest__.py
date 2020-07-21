# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright 2018 Odoo Helper
# See LICENSE file for full copyright and licensing details.
#
##############################################################################
{
    'name': 'Website Store Locater',
    'category': 'Website',
    'summary': 'Website Advance Product Search',

    'version': '0.1',
    'description': """
Website Advance Product Search
==================
        This module allows diffrent store location of Your Company or Branch
                placed into the map and easily Customer or Client get the Information and Reach you.
        """,

    'author': 'Odoo Helper',
    'license': 'AGPL-3',

    'depends': [
        'website'
        ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/assets.xml',
        'views/store_locator.xml',
        'views/store_country.xml',
        'views/template.xml',
    ],
    'images': ['images/OdooHelper.jpg'],
    'price': 48.28,
    'currency': 'USD',

    'installable': True,
    'application': False
}
