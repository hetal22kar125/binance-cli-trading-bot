import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from config import API_KEY, SECRET_KEY, BASE_URL

class BinanceClient:

    def _sign(self, params):
        query_string = urlencode(params)
        signature = hmac.new(
            SECRET_KEY.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()
        return signature

    def place_order(self, symbol, side, order_type, quantity, price=None):
        endpoint = "/fapi/v1/order"

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
            "timestamp": int(time.time() * 1000)
        }

        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        params["signature"] = self._sign(params)

        headers = {"X-MBX-APIKEY": API_KEY}

        response = requests.post(
            BASE_URL + endpoint,
            headers=headers,
            params=params
        )

        return response.json()