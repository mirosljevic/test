import os

risk_analyst = {
    "username": os.getenv("RISK_ANALYST", "auto_risk_analyst_5@pgp-ad.com"),
    "password": "User123456!!",
}

risk_analyst_2 = {
    "username": os.getenv("RISK_ANALYST_2", "auto_risk_analyst_4@pgp-ad.com"),
    "password": "User123456!!",
}

lottery_security_officer = {
    "username": os.getenv("LOT_SEC_OFFICER", "lot_sec_officer2@pgp-ad.com"),
    "password": "Test@1234",
}

risk_manager = {
    "username": os.getenv("RISK_MANAGER", "uat_risk_man2@pgp-ad.com"),
    "password": "Test@1234",
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
