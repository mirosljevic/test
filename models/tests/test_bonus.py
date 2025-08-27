import pytest
from models import Bonus, BonusType


class TestBonus:
    def test_bonus_creation(self):
        bonus = Bonus(
            bonus_type=BonusType.FREE_ROUNDS,
        )
        assert bonus.bonus_type == BonusType.FREE_ROUNDS
        assert bonus.bonus_id == BonusType.FREE_ROUNDS.bonus_id
        assert bonus.bonus_name == BonusType.FREE_ROUNDS.display_name


if __name__ == "__main__":
    pytest.main([__file__])
