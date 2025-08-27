import pytest
from datetime import datetime
from models import Player


class TestPlayer:
    def test_basic_player_creation(self):
        player = Player(first_name="John", last_name="Doe")
        assert player.first_name == "John"
        assert player.last_name == "Doe"
        assert player.full_name == "John Doe"

    def test_player_with_optional_fields(self):
        player = Player(
            first_name="Jane",
            last_name="Smith",
            email="jane@example.com",
            date_of_birth=datetime(1990, 1, 1),
        )
        assert player.email == "jane@example.com"
        assert player.age is not None

    def test_player_properties(self):
        player = Player(
            first_name="John",
            last_name="Doe",
            date_of_birth=datetime(1990, 1, 1),
            geolocation=(40.7128, -74.0060),
        )
        assert player.full_name == "John Doe"
        assert player.age > 0
        assert player.latitude == 40.7128
        assert player.longitude == -74.0060


if __name__ == "__main__":
    pytest.main([__file__])
