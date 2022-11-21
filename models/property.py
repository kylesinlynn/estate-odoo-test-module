# -*- coding: utf-8 -*-

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api

class Property(models.Model):
    _name = 'estate.property'
    _inherit = ['mail.thread']
    _description = 'Real Estate Property'
    
    pn = fields.Char('pn', readonly=True, required=True, copy=False, default='New')
    name = fields.Char('Title', required=True, track_visibility='always', translate=True)
    description = fields.Text('Description', track_visibility='always', translate=True)
    postcode = fields.Char('Postcode', track_visibility='always', translate=True)
    date_availability = fields.Date('Available From', default=lambda self: fields.Date.context_today(self) + relativedelta(months=3), copy=False, track_visibility='always')
    expected_price = fields.Float('Expected Price', required=True, track_visibility='always')
    selling_price = fields.Float('Selling Price', required=True, track_visibility='always')
    bedrooms = fields.Integer('Bedrooms', default=2, track_visibility='always')
    living_area = fields.Integer('Living Area (sqm)', track_visibility='always')
    facades = fields.Integer('Facades', track_visibility='always')
    garage = fields.Boolean('Garage', track_visibility='always')
    garden = fields.Boolean('Garden', track_visibility='always')
    garden_area = fields.Integer('Garden Area (sqm)', track_visibility='always')
    garden_orientation = fields.Selection(
        selection=[
            ('N', 'North'),
            ('S', 'South'),
            ('E', 'East'),
            ('W', 'West')
        ],
        string='Garden Orientation', track_visibility='always'
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
        default='new', track_visibility='always'
    )
    active = fields.Boolean('Active', default=True, track_visibility='always')
    
    property_type_id = fields.Many2one('estate.property.type', string='Property Type', track_visibility='always')
    tag_ids = fields.Many2many('estate.property.tag', string='Tags', track_visibility='always')
    
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
    
