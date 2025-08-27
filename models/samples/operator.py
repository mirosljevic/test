from models import Operator, OperatorRole


def main():
    operator = Operator(
        username="risk_analyst1",
        password="secure_password123",
        role=OperatorRole.RISK_ANALYST,
    )

    print(f"Operator: {operator.username}, Password: {operator.password}")
    print(f"Role: {operator.role}")
    print(f"Operator: {operator}")
    print(f"Operator as dict: {operator.__dict__}")


if __name__ == "__main__":
    main()
