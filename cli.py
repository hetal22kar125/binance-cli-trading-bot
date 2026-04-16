import argparse
from bot.orders import execute_order


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


def print_response(response):
    print("\n" + "=" * 45)
    print("📥 ORDER RESPONSE")
    print("=" * 45)

    if not response:
        print("❌ No response from server")
        return

    if "error" in response:
        print(f"❌ Error: {response['error']}")
    else:
        print("🚀 Order Placed Successfully!\n")
        print(f"Order ID     : {response.get('orderId')}")
        print(f"Symbol       : {response.get('symbol')}")
        print(f"Status       : {response.get('status')}")
        print(f"Side         : {response.get('side')}")
        print(f"Type         : {response.get('type')}")
        print(f"Executed Qty : {response.get('executedQty')}")
        print(f"Avg Price    : {response.get('avgPrice')}")

    print("=" * 45 + "\n")


def main():
    parser = argparse.ArgumentParser(description="Binance Futures CLI Trading Bot")

    parser.add_argument("--symbol", required=True, help="e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    # 🔥 Validation
    if args.quantity <= 0:
        print("❌ Quantity must be greater than 0")
        return

    if args.type == "LIMIT" and not args.price:
        print("❌ Price is required for LIMIT orders")
        return

    if args.price and args.price <= 0:
        print("❌ Price must be greater than 0")
        return

    # Request print
    print_request(args)

    # Execute order
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

    # Response print
    print_response(response)


if __name__ == "__main__":
    main()