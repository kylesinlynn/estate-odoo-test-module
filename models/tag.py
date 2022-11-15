# -*- coding: utf-8 -*-

from odoo import fields, models 

class Tag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Real Estate Property Tag'
    
    name = fields.Char('Name', required=True)
    color = fields.Integer('Color Index')