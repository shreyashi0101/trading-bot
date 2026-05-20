from bot.client import client
from bot.logging_config import logger

from binance.exceptions import BinanceAPIException
from requests.exceptions import RequestException


def place_order(symbol, side, order_type, quantity, price=None):

    try:

        logger.info(
            f"Placing order | {symbol} | {side} | {order_type} | qty={quantity} | price={price}"
        )

        params = {
            "symbol": symbol.upper(),
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        if order_type == "LIMIT":

            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logger.info(f"API RESPONSE: {response}")

        return response

    except BinanceAPIException as e:

        logger.error(f"Binance API Error: {e}")

        raise

    except RequestException as e:

        logger.error(f"Network Error: {e}")

        raise

    except Exception as e:

        logger.error(f"Unexpected Error: {e}")

        raise