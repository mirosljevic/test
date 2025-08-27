import os

risk_analyst = {
    "username": os.getenv("RISK_ANALYST", "oex2_risk_analyst2"),
    "password": "Test@1234",
}


risk_manager = {
    "username": os.getenv("RISK_MANAGER", "oex2_risk_man2"),
    "password": "Test@1234",
}

marketing_analyst = {
    "username": os.getenv("MARKETING_ANALYST", "oex2_mar_analyst2"),
    "password": "Test@1234",
}

control_room_operator = {
    "username": os.getenv("CONTROL_ROOM_OPERATOR", "oex2_cr_oper2"),
    "password": "Test@1234",
}

lottery_control_room_operator = {
    "username": os.getenv(
        "LOTTERY_CONTROL_ROOM_OPERATOR",
        "oex2_lot_cr_oper2"),
    "password": "Test@1234",
}

lottery_security_officer = {
    "username": os.getenv("LOTTERY_SECURITY_OFFICER", "oex2_lot_sec_off1"),
    "password": "Test@1234",
}

ilottery_security_officer = {
    "username": os.getenv("ILOTTERY_SECURITY_OFFICER", "oex2_ilot_sec_off1"),
    "password": "Test@1234",
}

lottery_operations_manager = {
    "username": os.getenv("LOTTERY_OPERATIONS_MANAGER", "oex2_lot_op_man1"),
    "password": "Test@1234",
}
