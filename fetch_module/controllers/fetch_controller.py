from odoo import http
from odoo.http import request
import requests
import json
from datetime import datetime
from efishery.auth_module.controlers.auth_controller import validate_token


class FishPriceController(http.Controller):

    @validate_token
    @http.route('/fetch-fish-price', auth='public', type='http')
    def fetch_fish_price(self):
        RESOURCE_URL = 'https://stein.efishery.com/v1/storages/5e1edf521073e315924ceab4/list'
        try:
            response = requests.get(RESOURCE_URL)
            if response.status_code == 200:
                data = response.json()
                fish_price_model = request.env['fish.price']
                data_success = 0
                for item in data:
                    uuid = item.get('uuid', None)
                    if not uuid:
                        continue
                    fish_price = fish_price_model.sudo().search([('uuid', '=', item.get('uuid'))], limit=1)
                    values = {
                        'uuid': item.get('uuid'),
                        'komoditas': item.get('komoditas'),
                        'area_provinsi': item.get('area_provinsi'),
                        'area_kota': item.get('area_kota'),
                        'size': item.get('size'),
                        'price': float(item.get('price', 0.0)),
                        'tgl_parsed': datetime.strptime(item.get('tgl_parsed'), '%Y-%m-%dT%H:%M:%SZ'),
                        'timestamp': item.get('timestamp')
                    }
                    try:
                        if fish_price:
                            continue
                        else:
                            fish_price_model.sudo().create(values)
                            data_success += 1
                    except Exception as e:
                        return http.Response(
                            json.dumps({'status': 'error', 'message': f"Error updating or creating record: {str(e)}"}),
                            content_type='application/json',
                        )
                return http.Response(
                    json.dumps({'status': 'success', 'message': '{} Data fetched successfully.'.format(data_success)}),
                    content_type='application/json',
                )
            else:
                return http.Response(
                    json.dumps({'status': 'error', 'message': 'Failed to fetch data from resource.'}),
                    content_type='application/json',
                )
        except Exception as e:
            return http.Response(
                json.dumps({'status': 'error', 'message': {str(e)}}),
                content_type='application/json',
            )
