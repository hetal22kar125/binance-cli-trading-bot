import argparse
from bot.orders import execute_order


def main():
    parser = argparse.ArgumentParser(
        description="Binance CLI Trading Bot"
    )

    parser.add_argument("--symbol", required=True, help="Trading pair (e.g. BTCUSDT)")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float, help="Required for LIMIT orders")

    args = parser.parse_args()

    if args.type == "LIMIT" and not args.price:
        print("❌ Price required for LIMIT orders")
        return

    print("\n📤 Order Request:")
    print(vars(args))

    response = execute_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price
    )

    print("\n📥 Response:")

    if "error" in response:
        print("❌ Error:", response["error"])
    else:
        print("✅ Success:", response)


if __name__ == "__main__":
    main()