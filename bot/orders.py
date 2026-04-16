from bot.client import BinanceClient
from logger import logger

client = BinanceClient()


def execute_order(symbol, side, order_type, quantity, price=None):
    logger.info(f"Placing order: {symbol} {side} {order_type}")

    response = client.place_order(
        symbol, side, order_type, quantity, price
    )

    if "error" in response:
        logger.error(f"Error placing order: {response}")
    else:
        logger.info(f"Order success: {response}")

    return response