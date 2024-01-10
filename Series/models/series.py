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
        logging.info(f'lo que quiera poner ++++++++{self}')
        logging.info(f'lo que quiera poner ++++++++{vals_lits[0]}')
        for add in vals_lits:
            logging.info(add)



        res = super(SeriesVarias, self).create(vals_lits)
        return res 
    def write(self, vals_lits):
        logging.info(f'lo que quiera poner parte 2**************{self}')
        logging.info(f'lo que quiera poner parte 2 **************{vals_lits}')

        logging.info({vals_lits.get('name')})
        logging.info(f'lo que quiera poner parte 2**************{self.category}')
        res = super().write(vals_lits)
        return res 

    @api.onchange('is_movie')  
    def onchange_movie(self):
        logging.info(self)

    def boton(self):
        logging.info('ver')
        
