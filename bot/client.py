import time
import hmac
import hashlib
import requests
from urllib.parse import urlencode
from config import API_KEY, SECRET_KEY, BASE_URL


class BinanceClient:

    def _sign(self, params):
        query_string = urlencode(params)
        return hmac.new(
            SECRET_KEY.encode(),
            query_string.encode(),
            hashlib.sha256
        ).hexdigest()

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

        try:
            response = requests.post(
                BASE_URL + endpoint,
                headers=headers,
                params=params
            )

            data = response.json()

            if response.status_code != 200:
                return {"error": data}

            return data

        except Exception as e:
            return {"error": str(e)}