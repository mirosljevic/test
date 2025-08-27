from api.executor import api
from environment import hosts


@api
def add_item(session, draw_count, game_id, wager_data, **kwargs):
    payload = {
        "wagerInfo": {
            "drawCount": draw_count,
            "gameId": game_id,
            "wagerData": wager_data
        }
    }
    return {
        "session": session,
        "method": "post",
        "host": hosts.gateway_web,
        "endpoint": "/web/shopping-cart/rest/v1/cart/item/",
        "json": payload,
        **kwargs
    }


@api
def order(session, **kwargs):
    payload = {"paymentId": "", "bonus": {"prizeId": "", "gameId": ""}}
    return {
        "session": session,
        "method": "post",
        "host": hosts.gateway_web,
        "endpoint": "/web/shopping-cart/rest/v1/cart/order",
        "json": payload,
        **kwargs
    }


@api
def get_cart_items(session, **kwargs):
    return {
        "session": session,
        "method": "get",
        "host": hosts.gateway_web,
        "endpoint": "/web/shopping-cart/rest/v1/cart",
        **kwargs
    }
