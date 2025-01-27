from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    truck_sale = fields.Many2one('truck.sale', "Truck Sale")

    
