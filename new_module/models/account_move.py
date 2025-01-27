from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    sale_truck = fields.Many2one('truck.sale', "Truck Sale")
