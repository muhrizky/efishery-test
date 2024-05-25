from odoo import models, fields, api
import requests
import time


class FishPrice(models.Model):
    _name = 'fish.price'
    _description = 'Fish Price'

    uuid = fields.Char(string='UUID', required=True)
    komoditas = fields.Char(string='Komoditas')
    area_provinsi = fields.Char(string='Area Provinsi')
    area_kota = fields.Char(string='Area Kota')
    size = fields.Char(string='Size')
    price = fields.Float(string='Price in IDR')
    tgl_parsed = fields.Datetime(string='Tanggal Parsed')
    timestamp = fields.Char(string='Timestamp')
    price_usd = fields.Float(string='Price in USD', compute='_compute_price_usd', store=True)

    _conversion_rate_cache = {'rate': None, 'timestamp': None}
    _cache_duration = 3600  # 1 hour in seconds

    @api.model
    def _get_conversion_rate(self):
        # Check if the cache is still valid
        current_time = time.time()
        if (self._conversion_rate_cache['timestamp'] is None or
                current_time - self._conversion_rate_cache['timestamp'] > self._cache_duration):
            # Fetch the conversion rate from the external API
            api_url = 'https://api.freecurrencyapi.com/v1/latest'
            params = {
                'apikey': 'fca_live_g7qLDMl24ab6RUS5my09h2pd0WqBPOovNd6Rj6kG',
                'base_currency': 'IDR',
                'currencies': 'USD'
            }
            response = requests.get(api_url, params=params)
            if response.status_code == 200:
                data = response.json()
                self._conversion_rate_cache['rate'] = data['data']['USD']
                self._conversion_rate_cache['timestamp'] = current_time
            else:
                raise Exception('Failed to fetch conversion rate')
        return self._conversion_rate_cache['rate']

    @api.depends('price')
    def _compute_price_usd(self):
        conversion_rate = self._get_conversion_rate()
        for record in self:
            record.price_usd = record.price * conversion_rate
