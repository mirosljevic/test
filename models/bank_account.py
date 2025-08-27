from dataclasses import dataclass
from typing import Optional


@dataclass
class BankAccount:
    account_number: str
    routing_number: str
    account_type: Optional[str] = None
    account_holder_name: Optional[str] = None

    def __str__(self) -> str:
        return f"{self.masked_account_number} (Routing: {self.masked_routing_number})"

    @property
    def masked_account_number(self) -> str:
        return f"****{self.account_number[-4:]}"

    @property
    def masked_routing_number(self) -> str:
        return f"****{self.routing_number[-4:]}"
