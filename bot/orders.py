import logging

def place_order(
    client,
    symbol,
    side,
    order_type,
    quantity,
    price=None
):

    try:

        request_data = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity
        }

        if order_type == "LIMIT":
            request_data["price"] = price
            request_data["timeInForce"] = "GTC"

        logging.info(f"REQUEST: {request_data}")

        response = client.futures_create_order(
            **request_data
        )

        logging.info(f"RESPONSE: {response}")

        return response

    except Exception as e:
        logging.error(str(e))
        raise
