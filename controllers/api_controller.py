# Odoo Modules
from odoo import _, http
from odoo.http import request

# Python Standar Modules
import json
from datetime import datetime

class ApiController(http.Controller):
    #routes = {
    #        'estate': {
    #                'property': '/property',
    #                'type': '/type',
    #                'tag': '/tag'
    #            }
    #        }

    fields = ['id', 'pn', 'name', 'description', 'postcode', 'date_availability',
            'expected_price', 'selling_price', 'bedrooms', 'living_area',
            'facades', 'garage', 'garden', 'garden_area', 'garden_orientation',
            'state', 'active', 'property_type_id', 'tag_ids']

    @staticmethod
    def make_dict(obj, create_update=False):
        try:
            fields = ApiController.fields[2:] if create_update else ApiController.fields[:]
            property = {str(key): obj[key] for key in fields if key in obj}
            #if create_update:
            #    property = {str(key): property[key] for key in property if key != 'id' and key != 'pn'}
            return property
        except Exception as error:
            print(error)

    # Retrieve All Estate Property
    @http.route('/estate', auth='public', methods=['GET'])
    def retrieve_all_properties(self, **kwargs):
        try:
            estate_properties = request.env['estate.property'].sudo().search([])

            properties = []
            for estate_property in estate_properties:
                properties.append(ApiController.make_dict(estate_property))

            return json.dumps(properties, default=str)
        except Exception as error:
            print(error)
            return json.dumps({'error': error}, default=str)

    # Create Property
    @http.route('/estate/create', auth='public', methods=['POST'], csrf=False)
    def create_property(self, **kwargs):
        try:
            property = ApiController.make_dict(request.env['estate.property'].sudo().create(ApiController.make_dict(kwargs,
                create_update=True)))

            return json.dumps(property, default=str)
        except Exception as error:
            print(error)
            return json.dumps({'error': error}, default=str)

    # Update Property
    @http.route('/estate/update', auth='public', methods=['PATCH'], csrf=False)
    def update_property(self, **kwargs):
        try:
            if 'id' not in kwargs:
                raise Exception("'id' is required to update a property!")
            print(ApiController.make_dict(kwargs))
            request.env['estate.property'].sudo().search([('id','=',kwargs['id'])]).write(ApiController.make_dict(kwargs, create_update=True))
            property = ApiController.make_dict(request.env['estate.property'].sudo().search([('id','=',kwargs['id'])]))
            return json.dumps(property, default=str)
        except Exception as error:
            print(error)
            return json.dumps({'error': error}, default=str)

    # Unlink Property
    @http.route('/estate/delete', auth='public', methods=['DELETE'], csrf=False)
    def unlink_property(self, **kwargs):
        try:
            if 'id' not in kwargs:
                raise Exception("'id' is required to delete a property!")
            request.env['estate.property'].sudo().search([('id','=',kwargs['id'])]).unlink()
            return json.dumps({'msg': 'deleted'}, default=str)
        except Exception as error:
            print(error)
            return json.dumps({'error': error}, default=str)
