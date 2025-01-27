from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    truck_sale = fields.Many2one('truck.sale', "Truck Sale")

    def action_confirm(self):
        res = super().action_confirm()
        for record in self:
            for rec in record.picking_ids:
                rec.write({'truck_sale': record.truck_sale.id})
        return res
