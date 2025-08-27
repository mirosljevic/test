import os

risk_analyst = {
    "username": os.getenv("RISK_ANALYST", "auto_risk_analyst_19@pgp-ad.com"),
    "password": "User1234567!",
}

risk_analyst_2 = {
    "username": os.getenv("RISK_ANALYST_2", "auto_risk_analyst_18@pgp-ad.com"),
    "password": "User1234567!",
}

lottery_security_officer = {
    "username": os.getenv("LOT_SEC_OFFICER", "auto_lott_sec_off1@pgp-ad.com"),
    "password": "User1234567!",
}

risk_manager = {
    "username": os.getenv("RISK_MANAGER", "auto_risk_man1@pgp-ad.com"),
    "password": "User1234567!",
}

control_room_operator = {
    "username": os.getenv("CONTROL_ROOM_OPERATOR", "gex2_cr_oper1@pgp-ad.com"),
    "password": "Test@1234",
}

lottery_control_room_operator = {
    "username": os.getenv(
        "LOTTERY_CONTROL_ROOM_OPERATOR", "gex2_lot_cr_oper1@pgp-ad.com"
    ),
    "password": "Test@1234",
}
