# -*- coding: utf-8 -*-

from odoo import models, fields 

class Type(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'
    
    name = fields.Char('Name', required=True)
    sequence = fields.Integer('Sequence', default=10)
    
    property_ids = fields.One2many('estate.property', 'property_type_id', string='Properties')