{
    'name':'Sale_Order_Report',
    'version': '17.0.1.0',
    'summary': 'Note',
    'description': """ Adding Base Setup """,
    'category':'Contact',
    'website':'www.asiamatrixsoftware.com',
    'email': 'info@asiamatrixsoftware.com',
    'license':"LGPL-3",
    'depends':[
        'base',
        'sale',
        'stock'
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
        'report/report.xml',
        'report/sale_order_report.xml',
    ],
    'installable':True,
    'application':False,
    'auto_install':False,
    
}