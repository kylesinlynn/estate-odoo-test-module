# -*- coding: utf-8 -*-

from odoo import models, fields 

class Type(models.Model):
    _name = 'estate.property.type'
    _description = 'Real Estate Property Type'
    
    name = fields.Char('Name', required=True, track_visibility='always')
    sequence = fields.Integer('Sequence', default=10, track_visibility='always')
    
    property_ids = fields.One2many('estate.property', 'property_type_id', string='Properties', track_visibility='always')
