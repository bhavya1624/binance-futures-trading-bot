import argparse

from bot.client import client
from bot.orders import place_order
from bot.validators import (
    validate_side,
    validate_order_type,
    validate_quantity
)
from bot.logging_config import setup_logger


def main():

    setup_logger()

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--symbol",
        required=True
    )

    parser.add_argument(
        "--side",
        required=True
    )

    parser.add_argument(
        "--type",
        required=True
    )

    parser.add_argument(
        "--quantity",
        type=float,
        required=True
    )

    parser.add_argument(
        "--price",
        type=float
    )

    args = parser.parse_args()

    try:

        validate_side(args.side)
        validate_order_type(args.type)
        validate_quantity(args.quantity)

        if args.type == "LIMIT" and not args.price:
            raise ValueError(
                "Price required for LIMIT order"
            )

        print("\n===== ORDER REQUEST =====")
        print(f"Symbol: {args.symbol}")
        print(f"Side: {args.side}")
        print(f"Type: {args.type}")
        print(f"Quantity: {args.quantity}")

        if args.price:
            print(f"Price: {args.price}")

        response = place_order(
            client,
            args.symbol,
            args.side,
            args.type,
            args.quantity,
            args.price
        )

        print("\n===== ORDER RESPONSE =====")
        print("Order ID:",
              response.get("orderId"))
        print("Status:",
              response.get("status"))
        print("Executed Qty:",
              response.get("executedQty"))
        print("Avg Price:",
              response.get("avgPrice"))

        print("\n✅ Order placed successfully")

    except Exception as e:
        print(f"\n❌ Error: {e}")


if __name__ == "__main__":
    main()
