from odoo import models, fields, api

class NewCity(models.Model):
    _name = 'new.city'
    _description = 'City'

    name = fields.Char('Name', copy=False)
    city_code = fields.Char('City Code')
    country = fields.Many2one('res.country', 'Country')
