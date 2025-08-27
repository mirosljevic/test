from api.executor import api
from environment import hosts


@api
def get_contracts(**kwargs):
    return {
        "method": "GET",
        "host": hosts.gateway_web,
        "endpoint": "/web/customer/rest/v1/contracts",
        **kwargs
    }


@api
def initiate_registration(session=None, email=None, **kwargs):
    return {
        "session": session,
        "method": "POST",
        "host": hosts.gateway_web,
        "endpoint": "/web/customer/rest/v2/players/initiate-registration",
        "json": {
            "email": email
        },
        **kwargs
    }


@api
def register_player(session=None,
                    email=None,
                    password=None,
                    first_name=None,
                    last_name=None,
                    date_of_birth=None,
                    identity_number_last_digits=None,
                    mobile_phone=None,
                    address1=None,
                    address2=None,
                    city=None,
                    zip_code=None,
                    state=None,
                    country=None,
                    personalised_offers=None,
                    contract_id=None,
                    gender=None,
                    request_id=None,
                    token=None,
                    channel=None,
                    **kwargs):
    return {
        "session": session,
        "method": "POST",
        "host": hosts.gateway_web,
        "endpoint": "/web/customer/rest/v2/players",
        "json": {
            "email": email,
            "password": password,
            "firstName": first_name,
            "lastName": last_name,
            "dateOfBirth": date_of_birth,
            "identityNumberLastDigits": identity_number_last_digits,
            "mobilePhone": mobile_phone,
            "address1": address1,
            "address2": address2,
            "city": city,
            "zip": zip_code,
            "state": state,
            "country": country,
            "personalisedOffers": personalised_offers,
            "contractId": contract_id,
            "gender": gender,
            "requestId": request_id,
            "token": token,
            "channel": channel
        },
        **kwargs
    }


@api
def get_player_levels(session):
    return {
        "session": session,
        "method": "GET",
        "host": hosts.gateway_web,
        "endpoint": "/web/customer/rest/v1/players/me/player-levels",
    }