{
    'name':'Township_Module',
    'version': '17.0.1.0',
    'summary': 'Note',
    'description': """ Township Module """,
    'category':'Contact',
    'website':'www.asiamatrixsoftware.com',
    'email': 'info@asiamatrixsoftware.com',
    'license':"LGPL-3",
    'depends':[
        'base',
        'city',
    ],
    'data':[
        'views/township_views.xml',
        'security/ir.model.access.csv',
        'views/township_contact_views.xml',
    ],
    'installable':True,
    'application':False,
    'auto_install':False,
    
}