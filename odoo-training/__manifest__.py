# -*- coding: utf-8 -*-
{
    'name': 'Odoo Training',
    'version': '14.0.0.0.1',
    'summary': 'Odoo Training',
    'depends': [
        'base',
        'mail',
        'web'
    ],
    'data': [
        'security/group.xml',
        'views/inherit_sales_order.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
