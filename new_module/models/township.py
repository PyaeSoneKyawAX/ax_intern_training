from odoo import models, fields

class NewTownship(models.Model):
    _name = 'new.township'
    _description = 'Township View'

    name = fields.Char('Name', copy=False)
    township_code = fields.Char('Township Code')
    city = fields.Many2one('new.city', 'City')
    country = fields.Many2one('res.country', 'Country')