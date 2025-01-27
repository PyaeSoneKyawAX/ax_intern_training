# -*- coding: utf-8 -*-
{
    'name': 'Base Setup',
    'version': '17.0.1.0',
    'summary': ' Note ',
    'description': """
        Adding Base Setup
    """,
    'category': 'Contact',
    'website': "www.asiamatrixsoftware.com",
    'email': 'info@asiamatrixsoftware.com',
    'license': "LGPL-3",
    'depends': [
        'base',
        'sale',
        'stock'
    ],
    'data': [
        'views/truck_sale_views.xml',
        'views/city_views.xml',
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/township_views.xml',
        'views/contact_form_views.xml',
        'views/account_view.xml',
        'views/stock_picking_views.xml',
        'reports/report.xml',
        'reports/sale_order_pdf.xml'

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
