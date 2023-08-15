# -*- coding: utf-8 -*-

{
    # Module Information
    'name': 'Website Product Variant Quote | Website Product Quote | Website Get Quote for Product Variant Odoo Shop',
    'category': 'Website/eCommerce',
    'summary': 'Request product quotation for variant, Easy to add product variant to get quotation reuqst and get quotation automatical, Choose variant to get variant wise quotation',
    'version': '16.0.0.0',
    "description": """
            product variant, variant quote for odoo shop,
            odoo shop,
            Request product quotation,
            Easy to add product to get quotation from the seller,
            Add product into quote cart using AJAX,
            Choose variant to get variant wise quotation,
            All in one for Product | Product Variant,
            Odoo website product quote,
            Quotation request,
            Odoo website Quote, Website product quote request, Website quote request,
            Website quotation request, website product quotation request, website get quote,
            website request quote,
            product quote,
            Quote quote, product variant quote,
            website product request,
            Variant wise add product to quote,
            website Request for quotation,
            request quotation,
            website ask for quote,
            website request a quote,
            Quotation send automatical,
            Quote send automatically,
            All in one Website Product Quote for Product | Product Variant
        
    """,
    'license': 'OPL-1',    
    'depends': ['website_sale','sale'],

    'data': [
        'data/data.xml',
        'data/mail_data.xml',
        'security/ir.model.access.csv',
        'views/product_view.xml',
        'views/quotation_request_view.xml',
        'templates/templates.xml',
    ],

    'assets':{
        'web.assets_frontend':[
        '/website_product_variant_quote_av/static/src/js/website_product_variant_quote_av.js',
        ]
    },

    #Odoo Store Specific
    'images': [
        'static/description/product_variant_quote.png',
    ],

    # Author
    'author': 'AV Technolabs',
    'website': 'http://avtechnolabs.com',
    'maintainer': 'AV Technolabs',

    # Technical
    'installable': True,
    'auto_install': False,
    'price': 16,
    "live_test_url":'https://www.youtube.com/watch?v=iLrcq-jvKIQ',
    'currency': 'EUR', 
}
