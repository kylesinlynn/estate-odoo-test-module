# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api

class Property(models.Model):
    _name = 'estate.property'
    _description = 'Real Estate Property'
    
    pn = fields.Char('pn', readonly=True, required=True, copy=False, default='New')
    name = fields.Char('Title', required=True)
    description = fields.Text('Description')
    postcode = fields.Char('Postcode')
    date_availability = fields.Date('Available From', default=lambda self: fields.Date.context_today(self) + relativedelta(months=3), copy=False)
    expected_price = fields.Float('Expected Price', required=True)
    selling_price = fields.Float('Selling Price', required=True)
    bedrooms = fields.Integer('Bedrooms', default=2)
    living_area = fields.Integer('Living Area (sqm)')
    facades = fields.Integer('Facades')
    garage = fields.Boolean('Garage')
    garden = fields.Boolean('Garden')
    garden_area = fields.Integer('Garden Area (sqm)')
    garden_orientation = fields.Selection(
        selection=[
            ('N', 'North'),
            ('S', 'South'),
            ('E', 'East'),
            ('W', 'West')
        ],
        string='Garden Orientation'
    )
    state = fields.Selection(
        selection=[
            ('new', 'New'),
            ('offer_received', 'Offer Received'),
            ('offer_accepted', 'Offer Accepted'),
            ('sold', 'Sold'),
            ('canceled', 'Canceled')
        ],
        string='Status',
        required=True,
        copy=False,
        default='new'
    )
    active = fields.Boolean('Active', default=True)
    
    property_type_id = fields.Many2one('estate.property.type', string='Property Type')
    tag_ids = fields.Many2many('estate.property.tag', string='Tags')
    
    def action_sold(self):
        self.write({'state': 'sold'})
        
    def action_cancel(self):
        self.write({'state': 'canceled'})
        
    @api.model 
    def create(self, vals):
        if vals.get('pn', 'New') == 'New':
            vals['pn'] = self.env['ir.sequence'].next_by_code('estate.property.sequence') or 'New'
        result = super(Property, self).create(vals)
        return result
    