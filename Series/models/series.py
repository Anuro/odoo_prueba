from odoo import _, api, fields, models, tools
from odoo.osv import expression
from odoo.exceptions import AccessError, UserError, ValidationError

class SeriesVarias(models.Model):
    _name = "gsm.series"

    name = fields.Char(string="Nombre")
    number = fields.Integer(string="Numero", default= 100)
    total = fields.Float(required= True, readonly = True)
    is_movie = fields.Boolean()
    category = fields.Selection([('terror1', 'Terror'),
                                ('comedia2', 'Comedia')])

    texto = fields.Html()
    fecha = fields.Datetime()
    imagen = fields.Binary()
    text = fields.Text()