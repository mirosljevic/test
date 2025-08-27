import pytest
from models import BankAccount


class TestBankAccount:
    def test_basic_bank_account_creation(self):
        account = BankAccount(
            account_number="1234567890123456", routing_number="121000248"
        )
        assert account.account_number == "1234567890123456"
        assert account.routing_number == "121000248"

    def test_bank_account_methods(self):
        account = BankAccount(
            account_number="1234567890123456", routing_number="121000248"
        )
        assert account.masked_account_number == "****3456"
        assert account.masked_routing_number == "****0248"


if __name__ == "__main__":
    pytest.main([__file__])
