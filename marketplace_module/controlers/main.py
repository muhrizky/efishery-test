from odoo import http
from odoo.http import request, Response
from odoo.addons.auth_module.controlers.auth_controller import validate_token
import json
from redis import Redis
import logging
from odoo.tools import config

_logger = logging.getLogger(__name__)


class MarketplaceController(http.Controller):
    @validate_token
    @http.route('/marketplace/order', type='json', auth='public', methods=['POST'], csrf=False)
    def create_order(self, **kwargs):
        order_data = request.jsonrequest
        try:
            sale_order, invoice, payment = request.env['sale.order'].sudo().create_sale_order(order_data)
            return {
                'sale_order_id': sale_order.id,
                'invoice_id': invoice.id,
                'payment_id': payment.id,
            }
        except Exception as e:
            return json.dumps({'error': e.name})

    @validate_token
    @http.route('/marketplace/sale_orders', type='http', auth='public', methods=['GET'], csrf=False)
    def list_sale_orders(self, **kwargs):
        is_from_redis = False
        try:
            # Get Redis configuration from Odoo config file
            redis_host = config.get('redis_host', '127.0.0.1')
            redis_port = int(config.get('redis_port', 6379))
            client = Redis(
                host=redis_host,
                port=redis_port
            )
            key = 'sale_orders'
            sale_order_redis = client.get(key)
            if sale_order_redis:
                result = json.loads(sale_order_redis.decode('utf-8'))
                is_from_redis = True
            else:
                result = self.get_sale_order_data()
                if result:
                    client.set(key, json.dumps(result), ex=30)
                    _logger.info("Sale Order Created from redis :%s, %s" % (key, result))
        except Exception as err:
            return Response(json.dumps({'error': str(err)}), content_type='application/json',
                            status=500)
        if result:
            result = [{**res, 'is_from_redis': is_from_redis} for res in result]
            return Response(json.dumps(result), content_type='application/json', status=200)

        return Response(json.dumps({"error": "No result found"}), content_type='application/json', status=404)

    def get_sale_order_data(self):
        domain = [('note', '=', 'From API Create Order')]
        sale_orders = request.env['sale.order'].sudo().search(domain)
        sale_order_data = []
        for order in sale_orders:
            sale_order_data.append({
                'sale_order_id': order.id,
                'customer': order.partner_id.name,
                'order_date': order.date_order.strftime('%Y-%m-%d %H:%M:%S'),
            })
        return sale_order_data
