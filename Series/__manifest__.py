# -*- coding:utf-8 -*-
{
    'name': 'Seriea',
    'summary': """
        Módulo que implementa el catálogo de series""",
    'website': "https://www.gasomarshal.com",
    'depends': [

    ],
    'author': 'Aldo Mex',
    "license": "LGPL-3",
    'category': 'Series',
    'description': '''
    Agrega un nuevo campo en la sección de series donde permite seleccionar de un catálogo series
    ''',
    'data': [
        
        'views/series_view.xml',
        'views/serires_menu.xml',
        'security/ir.model.access.csv'

    ],
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,
}