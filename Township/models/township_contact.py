from odoo import models, fields


class township_contact(models.Model):
    _inherit = 'res.partner'

    township_contact = fields.Many2one('township.contact', "Township")

