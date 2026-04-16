import argparse
import logging
from bot.orders import execute_order

# ----------------------------
# LOGGING SETUP (bot.log file)
# ----------------------------
logging.basicConfig(
    filename="bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def print_request(args):
    print("\n" + "=" * 45)
    print("📤 ORDER REQUEST")
    print("=" * 45)
    print(f"Symbol   : {args.symbol}")
    print(f"Side     : {args.side}")
    print(f"Type     : {args.type}")
    print(f"Quantity : {args.quantity}")
    print(f"Price    : {args.price}")
    print("=" * 45)

    # LOG REQUEST
    logging.info(
        f"ORDER REQUEST -> symbol={args.symbol}, side={args.side}, "
        f"type={args.type}, quantity={args.quantity}, price={args.price}"
    )


def print_response(response):
    print("\n" + "=" * 45)
    print("📥 ORDER RESPONSE")
    print("=" * 45)

    if not response:
        print("❌ No response from server")
        logging.error("EMPTY RESPONSE FROM SERVER")
        return

    if "error" in response:
        print(f"❌ Error: {response['error']}")
        logging.error(f"ORDER ERROR -> {response['error']}")
    else:
        print("🚀 Order Placed Successfully!\n")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Symbol       : {response.get('symbol')}")
        print(f"Status       : {response.get('status')}")
        print(f"Side         : {response.get('side')}")
        print(f"Type         : {response.get('type')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice')}")

        # LOG SUCCESS RESPONSE
        logging.info(f"ORDER SUCCESS -> {response}")

    print("=" * 45 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    # ----------------------------
    # VALIDATION
    # ----------------------------
    if args.quantity <= 0:
        print("❌ Quantity must be greater than 0")
        logging.error("INVALID QUANTITY")
        return

    if args.type == "LIMIT" and not args.price:
        print("❌ Price is required for LIMIT orders")
        logging.error("LIMIT ORDER WITHOUT PRICE")
        return

    if args.price and args.price <= 0:
        print("❌ Price must be greater than 0")
        logging.error("INVALID PRICE")
        return

    # ----------------------------
    # EXECUTE ORDER
    # ----------------------------
    print_request(args)

    try:
        response = execute_order(
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )
    except Exception as e:
        response = {"error": str(e)}
        logging.error(f"EXCEPTION -> {str(e)}")

    print_response(response)


if __name__ == "__main__":
    main()