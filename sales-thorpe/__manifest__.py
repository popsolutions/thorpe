{
    'name': 'Sales Thorpe',
    'version': '1.0',
    'summary': 'Trigger sales automated PVE deploy integration',
    'description': 'Custom module to trigger actions on sales order confirmation and automate PVE deploy integration.',
    'category': 'Sales',
    'author': 'Marcos Méndez & Enieber Cunha | pop.coop',
    'depends': ['sale, sale_management'],
    'data': [
        'views/sales_order_view.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
}
