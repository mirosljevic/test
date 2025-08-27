import pytest
from models import InstantGame, GameType


class TestInstantGame:
    def test_basic_instant_game_creation(self):
        game = InstantGame(game_type=GameType.PRIMETIME_PAYOUT)
        assert game.game_type == GameType.PRIMETIME_PAYOUT
        assert game.game_name == "Primetime Payout"

    def test_instant_game_properties(self):
        game = InstantGame(
            game_type=GameType.DRAGON_BLAST,
            price=5.0,
            available_bets=[
                1.0,
                5.0])
        assert game.game_id == "DRAGONBLAST"
        assert game.price == 5
        assert 5 in game.available_bets


if __name__ == "__main__":
    pytest.main([__file__])
