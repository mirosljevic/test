from dataclasses import dataclass
from typing import Optional


@dataclass
class CreditCard:
    number: str
    expiry_month: str
    expiry_year: str
    cvv: str
    cardholder_name: Optional[str] = None
    card_type: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.masked_number} ({self.card_type or self.detect_card_type()})"

    def detect_card_type(self) -> str:
        if self.number.startswith("4"):
            return "Visa"
        elif self.number.startswith(("51", "52", "53", "54", "55")):
            return "MasterCard"
        elif self.number.startswith(("34", "37")):
            return "American Express"
        elif self.number.startswith("6011"):
            return "Discover"
        else:
            return "Unknown"

    @property
    def masked_number(self) -> str:
        return f"****-****-****-{self.number[-4:]}"

    @property
    def expiry_full_year(self) -> str:
        return f"{self.expiry_month}/{self.expiry_year}"

    @property
    def expiry_short_year(self) -> str:
        return f"{self.expiry_month}/{self.expiry_year[-2:]}"
