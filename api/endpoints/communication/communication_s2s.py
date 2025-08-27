from api.executor import api
from environment import hosts


@api
def send_external_message(access_token, mail, event_name, message_type, event_owner, user_id, actor,
                          attachments=None, parameters=None):
    payload = {
        "recipients": [
            {
                "messageType": message_type,
                "userId": user_id,
                "toAddress": mail,
                "actor": actor
            }
        ],
        "eventName": event_name,
        "eventOwner": event_owner,
        "attachments": attachments or [],
        "parameters": parameters or {}
    }
    return {
        "method": "POST",
        "host": hosts.api,
        "endpoint": "/api/communication/rest/v1/messages",
        "bearer_token": access_token,
        "json": payload
    }
