{
    'name': "Thorpe Base",
    'version': '1.0',
    'summary': "Um módulo básico para Thorpe",
    'sequence': 10,
    'description': """
        Descrição longa do Thorpe Base.
        Este módulo fornece uma base para funcionalidades específicas do Thorpe.
    """,
    'author': 'Marcos Méndez & Enieber Cunha | pop.coop',
    'category': 'Applications',
    'license': 'AGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/ir.model.access.csv',
	    'views/thorpe_cluster.xml',
	    'views/cron_update_list_node.xml',
	    'views/cron_update_list_storage.xml',
	    'views/cron_update_list_image.xml',
	    'views/thorpe_node.xml',
	    'views/thorpe_storage.xml',
	    'views/thorpe_image.xml',
	    'views/menu.xml',
    ],
    'demo': [
    ],
    'images': ['static/img/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
