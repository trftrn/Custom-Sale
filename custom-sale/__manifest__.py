{
    'name': 'Custom Sale',
    'version': '14.0.0.1',
    'summary': 'coba custom sale',
    'description': 'coba doang custom sale',
    'category': 'technical',
    'author': 'vini',
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'security/group.xml',
        'view/custom-saleorder-view.xml',
        'view/customer_vvip.xml',
        'view/inherit_customer_customer_vvip.xml'
    ],
    # 'demo': [''],
    'installable': True,
    'auto_install': False,

}