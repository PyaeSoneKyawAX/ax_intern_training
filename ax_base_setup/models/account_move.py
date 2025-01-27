from odoo import models, fields, api, _

class AccountMove(models.Model):
    _inherit = 'account.move'

    truck_sale = fields.Many2one('truck.sale', "Truck Sale")
