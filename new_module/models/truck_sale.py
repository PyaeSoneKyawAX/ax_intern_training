from odoo import models, fields, api

class TruckSale(models.Model):
    _name = 'truck.sale'
    _description = "Truck Sale"

    name = fields.Char("Name")
    customer = fields.Many2one('res.partner', "Customer")
    expiration = fields.Date("Expiration")
    line_id = fields.One2many('truck.sale.line', 'truck', "Line")
    amount_total = fields.Float("Total", compute="_compute_amount_total", store=True)

    @api.depends('line_id.total')
    def _compute_amount_total(self):
        for rec in self:
            rec.amount_total = sum(line.total for line in rec.line_id)


class TruckSaleLine(models.Model):
    _name = 'truck.sale.line'
    _description = "Truck Sale Line"

    product_id = fields.Many2one(comodel_name='product.product', string="Product")
    name = fields.Char("Description",)
    uom = fields.Many2one('uom.uom', "Unit Of Measure")
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

    @api.onchange('quantity', 'unit_price')
    def _compute_total(self):
        for rec in self:
            if rec.quantity or rec.unit_price:
                rec.total = rec.quantity * rec.unit_price
