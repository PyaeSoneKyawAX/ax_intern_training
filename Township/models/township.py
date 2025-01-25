from odoo import models,fields

class Township(models.Model):
    _name= 'township.contact'
    _description = "township Contact"
    
    name=fields.Char("Name")
    
    township_code = fields.Char("Township Code")
    
    city=fields.Many2one('city.contact',"City")
    
    country = fields.Many2one('res.country',"Country")