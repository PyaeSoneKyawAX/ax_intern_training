from odoo import models, fields, api, _

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    truck_sale = fields.Many2one('truck.sale', "Truck Sale")

    
class TruckNote(models.Model):
    
    _inherit = 'stock.move'
    
    truck_sale_note = fields.Text(
        string="Truck Sale Note",
        store=True
    )
