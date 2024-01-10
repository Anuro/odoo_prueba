from odoo import _, api, fields, models, tools
from odoo.osv import expression
from odoo.exceptions import AccessError, UserError, ValidationError
import logging 

_logger= logging.getLogger(__name__) 

class SeriesVarias(models.Model):
    _name = "gsm.series"

    name = fields.Char(string="Nombre",required= True)
    number = fields.Integer(string="Numero", default= 100)
    total = fields.Float(readonly = True)
    is_movie = fields.Boolean()
    category = fields.Selection([('terror1', 'Terror'),
                                ('comedia2', 'Comedia')])

    texto = fields.Html()
    fecha = fields.Datetime()
    imagen = fields.Binary()
    text = fields.Text()

    @api.model_create_multi  #funsion de afuersas para crear create
    def create (self, vals_lits):
        logging.info("lo que tu quieras")

        res = super(SeriesVarias, self).create(vals_lits)
        return res 
    def write(self, vals_lits):
        logging.info("lo que quieras part 2")

        res = super().write(vals_lits)
        return res 