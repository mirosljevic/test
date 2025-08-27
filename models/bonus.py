from dataclasses import dataclass
from typing import Optional
from enum import Enum


class BonusType(Enum):
    FREE_ROUNDS = ("FREE_ROUNDS", "Free Rounds")
    PLAY_CREDIT = ("PLAY_CREDIT", "Play Credit")
    CASH_CREDIT = ("CASH_CREDIT", "Cash Credit")
    FUNDS_MATCHUP = ("FUNDS_MATCHUP", "Funds Matchup")

    def __init__(self, bonus_id: str, display_name: str):
        self.bonus_id = bonus_id
        self.display_name = display_name

    def __str__(self) -> str:
        return self.display_name


@dataclass
class Bonus:
    bonus_type: BonusType
    status: Optional[str] = None
    allowed_games: Optional[list] = None
    amount_type: Optional[str] = None
    cost_per_ticket: Optional[float] = None
    number_of_rounds: Optional[int] = None
    number_of_tickets: Optional[int] = None
    total_amount: Optional[float] = None

    def __str__(self) -> str:
        return f"{self.bonus_name} (Id: {self.bonus_id})"

    @property
    def bonus_id(self) -> str:
        return self.bonus_type.bonus_id

    @property
    def bonus_name(self) -> str:
        return self.bonus_type.display_name
