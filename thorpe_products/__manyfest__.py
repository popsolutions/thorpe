{
    'name': "Thorpe Products",
    'version': '1.0',
    'summary': "Thorpe product template",
    'sequence': 11,
    'description': """
        Descrição longa do Thorpe Products.
        Este módulo fornece uma base para funcionalidades específicas do Thorpe.
    """,
    'author': 'Marcos Méndez & Enieber Cunha | pop.coop',
    'category': 'Applications',
    'license': 'AGPL-3',
    'depends': ['thorpe'],
    'data': [
	    'demo/thorpe_vm.xml',
        'demo/thorpe_lxc.xml',
    ],
    'demo': [],
    'images': ['static/img/icon.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
