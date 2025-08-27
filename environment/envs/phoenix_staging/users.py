import os

risk_analyst = {
    "username": os.getenv("RISK_ANALYST", "uat_risk_analyst2@phxpbl.com"),
    "password": "password1234$",
}

risk_analyst_2 = {
    "username": os.getenv("RISK_ANALYST_2", "journey004analyst@phxpbl.com"),
    "password": "Test@1234",
}

lottery_security_officer = {
    "username": os.getenv(
        "LOT_SEC_OFFICER",
        "bo1_lot_sec_officer1@phxpbl.com"),
    "password": "SmuSmu.12345",
}

risk_manager = {
    "username": os.getenv("RISK_MANAGER", "risk_manager1@phxpbl.com"),
    "password": "password1234$",
}

marketing_analyst = {
    "username": os.getenv("MARKETING_ANALYST", "plex_mar_analyst1@phxpbl.com"),
    "password": "Test@1234",
}

control_room_operator = {
    "username": os.getenv("CONTROL_ROOM_OPERATOR", "gex2_cr_oper1@phxpbl.com"),
    "password": "Test@1234",
}

lottery_control_room_operator = {
    "username": os.getenv(
        "LOTTERY_CONTROL_ROOM_OPERATOR", "gex2_lot_cr_oper1@phxpbl.com"
    ),
    "password": "Test@1234",
}
