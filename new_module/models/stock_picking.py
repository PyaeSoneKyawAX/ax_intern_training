from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'stock.picking'

    truck_sale = fields.Many2one('truck.sale', "Truck Sale")

    truck_sale_note = fields.Text(
        string="Truck Sale Note",
        store=True
    )

class RemarkLine(models.Model):
    _inherit = 'stock.move'

    remark_line = fields.Char('Remark', store=True)