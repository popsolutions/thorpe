{
    'name': "Thorpe Base",
    'version': '1.0',
    'summary': "Um módulo básico para Thorpe",
    'sequence': 10,
    'description': """
        Descrição longa do Thorpe Base.
        Este módulo fornece uma base para funcionalidades específicas do Thorpe.
    """,
    'author': "Seu Nome",
    'website': "http://seuwebsite.com",
    'category': 'Applications',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
	'views/menu.xml',
    ],
    'demo': [
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
