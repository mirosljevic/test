import os

risk_analyst = {
    "username": os.getenv("RISK_ANALYST", "plex_risk_analyst1@phxpbl.com"),
    "password": "Test@1234",
}


risk_manager = {
    "username": os.getenv("RISK_MANAGER", "plex1_risk_man1@phxpbl.com"),
    "password": "Test@1234",
}

marketing_analyst = {
    "username": os.getenv("MARKETING_ANALYST", "plex_mar_analyst1@phxpbl.com"),
    "password": "Test@1234",
}

control_room_operator = {
    "username": os.getenv("CONTROL_ROOM_OPERATOR", "plex_cr_oper1@phxpbl.com"),
    "password": "Test@1234",
}

lottery_control_room_operator = {
    "username": os.getenv(
        "LOTTERY_CONTROL_ROOM_OPERATOR", "plex_lot_cr_oper1@phxpbl.com"
    ),
    "password": "Test@1234",
}
