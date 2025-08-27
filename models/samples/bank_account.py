from models import BankAccount


def main():
    account = BankAccount(
        account_number="1234567890123456",
        routing_number="121000248",
        account_type="checking",
        account_holder_name="John Doe",
    )

    print(f"Account: {account}")
    print(f"Type: {account.account_type}")


if __name__ == "__main__":
    main()
