from odoo import http
from odoo.http import request, Response
from efishery.auth_module.controlers.auth_controller import validate_token
import json


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
        try:
            # Fetch list of sale orders
            domain = [('note', '=', 'From API Create Order')]
            sale_orders = request.env['sale.order'].sudo().search(domain)
            sale_order_data = []
            for order in sale_orders:
                sale_order_data.append({
                    'sale_order_id': order.id,
                    'customer': order.partner_id.name,
                    'order_date': order.date_order.strftime('%Y-%m-%d %H:%M:%S'),
                })
            return json.dumps({'sale_order': sale_order_data})
        except Exception as e:
            return json.dumps({'error': str(e)})
