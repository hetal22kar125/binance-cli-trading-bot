from bot.client import BinanceClient
from logger import logger

client = BinanceClient()

def execute_order(symbol, side, order_type, quantity, price=None):
    try:
        logger.info(f"Placing order: {symbol} {side} {order_type}")

        response = client.place_order(
            symbol, side, order_type, quantity, price
        )

        logger.info(f"Response: {response}")

        return response

    except Exception as e:
        logger.error(f"Error: {str(e)}")
        return {"error": str(e)}