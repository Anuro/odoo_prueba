from odoo import _, api, fields, models, tools
from odoo.osv import expression
from odoo.exceptions import AccessError, UserError, ValidationError

class PeliculasCine(models.Model):
    _name = "gsm.peliculas"

    name = fields.Char()
    number = fields.Integer()
    total = fields.Float()
    is_movie = fields.Boolean()
    category = fields.Selection([('terror1', 'Terror'),
                                ('comedia2', 'Comedia')])

    texto = fields.Html()
    fecha = fields.Datetime()
    imagen = fields.Binary()
    text = fields.Text()

