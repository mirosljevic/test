import pytest
from models import CreditCard


class TestCreditCard:
    def test_basic_credit_card_creation(self):
        card = CreditCard(
            number="4111111111111111",
            expiry_year="2026",
            expiry_month="12",
            cvv="123",
            cardholder_name="John Doe",
            card_type="Visa"
        )
        assert card.card_type == "Visa"
        assert card.cardholder_name == "John Doe"

    def test_credit_card_methods(self):
        card = CreditCard(
            number="4111111111111111",
            expiry_year="2026",
            expiry_month="12",
            cvv="123",
            cardholder_name="John Doe",
        )
        assert card.masked_number == "****-****-****-1111"
        assert card.detect_card_type() == "Visa"


if __name__ == "__main__":
    pytest.main([__file__])
