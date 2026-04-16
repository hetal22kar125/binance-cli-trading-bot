from bot.client import BinanceClient
from logger import logger

client = BinanceClient()


def execute_order(symbol, side, order_type, quantity, price=None):
    logger.info(f"Placing order | {symbol} | {side} | {order_type}")

    # basic validation
    if quantity <= 0:
        error_msg = "Quantity must be greater than 0"
        logger.error(error_msg)
        return {"error": error_msg}

    if order_type == "LIMIT" and not price:
        error_msg = "Price required for LIMIT order"
        logger.error(error_msg)
        return {"error": error_msg}

    try:
        response = client.place_order(
            symbol, side, order_type, quantity, price
        )
    except Exception as e:
        logger.error(f"API exception: {str(e)}")
        return {"error": str(e)}

    if "error" in response:
        logger.error(
            f"Order failed | {symbol} | {side} | {order_type} | {response.get('error')}"
        )
    else:
        logger.info(
            f"Order success | {symbol} | {side} | {order_type} | qty={quantity} | price={price}"
        )

    return response