import os

risk_analyst = {
    "username": os.getenv("RISK_ANALYST", "gex2_risk_analyst2"),
    "password": "Test@1234",
}


risk_manager = {
    "username": os.getenv("RISK_MANAGER", "gex2_risk_man2"),
    "password": "Test@1234",
}

marketing_analyst = {
    "username": os.getenv("MARKETING_ANALYST", "gex2_mar_analyst2"),
    "password": "Test@1234",
}

control_room_operator = {
    "username": os.getenv("CONTROL_ROOM_OPERATOR", "gex2_cr_oper2"),
    "password": "Test@1234",
}

lottery_control_room_operator = {
    "username": os.getenv(
        "LOTTERY_CONTROL_ROOM_OPERATOR",
        "gex2_lot_cr_oper2"),
    "password": "Test@1234",
}
