from models.operator import Operator, OperatorRole
from mongo import OperatorMongoClient

operators = [
    ("journey001analyst@phxpbl.com", "Test@1234", OperatorRole.RISK_ANALYST),
    ("journey002analyst@phxpbl.com", "Test@1234", OperatorRole.RISK_ANALYST),
    ("journey003analyst@phxpbl.com", "Test@1234", OperatorRole.RISK_ANALYST),
    ("journey004analyst@phxpbl.com", "Test@1234", OperatorRole.RISK_ANALYST),
    ("journey005analyst@phxpbl.com", "Test@1234", OperatorRole.RISK_ANALYST),
    ("journey006analyst@phxpbl.com", "Test@1234", OperatorRole.RISK_ANALYST),
    ("journey007analyst@phxpbl.com", "Test@1234", OperatorRole.RISK_ANALYST),
    ("journey008analyst@phxpbl.com", "Test@1234", OperatorRole.RISK_ANALYST),
    ("journey009analyst@phxpbl.com", "Test@1234", OperatorRole.RISK_ANALYST),
]


def main():
    for operator in operators:
        user, password, role = operator
        operator_instance = Operator(username=user, password=password, role=role)
        operator_client = OperatorMongoClient(operator=operator_instance)
        operator_client.insert()


if __name__ == "__main__":
    main()
