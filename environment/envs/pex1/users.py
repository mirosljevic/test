import os

marketing_analyst = {
    "username": os.getenv("MARKETING_ANALYST", "pex2_mar_analyst2"),
    "password": "Test@1234",
}

risk_analyst = {
    "username": os.getenv("RISK_ANALYST", "uat_risk_analyst2"),
    "password": "password1234$",
}
