import pytest
from models import DrawGame, DrawGameType


class TestDrawGame:
    def test_basic_draw_game_creation(self):
        game = DrawGame(game_type=DrawGameType.POWERBALL)
        assert game.game_type == DrawGameType.POWERBALL
        assert game.game_name == "Powerball"

    def test_draw_game_properties(self):
        game = DrawGame(
            game_type=DrawGameType.MEGA_MILLIONS,
            ticket_price=2.0,
            draw_id="DRAW_001")
        assert game.game_id == "MEGAMILLIONS"
        assert game.ticket_price == 2
        assert game.draw_id == "DRAW_001"


if __name__ == "__main__":
    pytest.main([__file__])
