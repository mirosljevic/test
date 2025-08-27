from datetime import datetime
from api.executor import api
from environment import hosts, credentials


@api
def create_offer(campaign_id, player_id, bonus_id, **kwargs):
    payload = {
        "players": [{
            "playerId": str(player_id),
            "bonusId": str(bonus_id)
        }],
        "campaignId": campaign_id,
        "status": "OFFER",
        "timestamp": datetime.utcnow().isoformat(timespec='microseconds') + 'Z',
    }
    return {
        "host": hosts.exponea,
        "method": "post",
        "endpoint": "/api/exponea/rest/v1/bonus-offer",
        "json": payload,
        "basic_auth_encoded": credentials.exponea_token,
        **kwargs
    }


@api
def achieve_bonus(campaign_id, player_id, bonus_id, condition=None, amount=None, **kwargs):
    payload = {
        "playerId": player_id,
        "bonusId": bonus_id,
        "campaignId": campaign_id,
        "status": "ACHIEVED",
        "timestamp": datetime.utcnow().isoformat(timespec='microseconds') + 'Z',
    }
    return {
        "host": hosts.exponea,
        "method": "post",
        "endpoint": "/api/exponea/rest/v1/bonus-achieve",
        "json": payload,
        "basic_auth_encoded": credentials.exponea_token,
        **kwargs
    }