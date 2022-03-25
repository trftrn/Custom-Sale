# -*- coding: utf-8 -*-
{
    'name': 'Odoo Training',
    'version': '14.0.0.0.1',
    'summary': 'Odoo Training',
    'depends': [
        'sale'
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/customer_vvip.xml',
        'views/inherit_sales_customer_view.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
