{
    'name': "Thorpe Base",
    'version': '1.0',
    'summary': "The base thorpe project for api connect to proxmox",
    'sequence': 10,
    'description': """
        Thorpe base
        This module create configuration to api proxmox connect.
    """,
    'author': 'Marcos Méndez & Enieber Cunha | pop.coop',
    'category': 'Applications',
    'license': 'AGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
	    'views/thorpe_base.xml',
	    'data/ir_cron_nodes.xml',
	    'data/ir_cron_storages.xml',
	    'views/thorpe_nodes.xml',
	    'views/thorpe_storages.xml',
	    'views/menu.xml',
    ],
    'images': ['static/img/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
