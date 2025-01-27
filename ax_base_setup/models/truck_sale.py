from odoo import models, fields, api, _

class TruckSale(models.Model):
    _name = 'truck.sale'
    _description = "Truck Sale"

    name = fields.Char("Name")
    customer = fields.Many2one('res.partner', "Customer")
    expiration = fields.Date("Expiration")
    line_id = fields.One2many('truck.sale.line', 'truck', "Line")

class TruckSaleLine(models.Model):
    _name = 'truck.sale.line'
    _description = "Truck Sale Line"

    product_id = fields.Many2one(comodel_name='product.product', string="Product_id")
    name = fields.Char("Description",)
    uom = fields.Many2one('uom.uom', "Unit Of Messure")
    quantity = fields.Float("Quantity")
    unit_price = fields.Float("Unit Price",)
    total = fields.Float("Total", compute="_compute_total")
    truck = fields.Many2one('truck.sale', "line_id", ondelete='cascade')

    @api.onchange('product_id')
    def _onchange_name_uom(self):
        for rec in self:
            if not rec.product_id:
                continue
            rec.name = rec.product_id.name
            rec.uom = rec.product_id.uom_id.id
            rec.unit_price = rec.product_id.lst_price

    def _compute_total(self):
        for rec in self:
            if rec.quantity or rec.unit_price:
                rec.total = rec.quantity * rec.unit_price
