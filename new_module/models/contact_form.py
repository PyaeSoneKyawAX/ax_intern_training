from odoo import models, fields

class Partner(models.Model):
    _inherit = 'res.partner'

    city_form = fields.Many2one('new.city', 'City')
    township_form = fields.Many2one('new.township', 'Township')