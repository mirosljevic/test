from datetime import datetime
from models import Player


def main():
    player = Player(
        first_name="John",
        last_name="Doe",
        email="john.doe@example.com",
        date_of_birth=datetime(1990, 5, 15),
        geolocation=(40.7128, -74.0060),
    )

    print(f"Player: {player.full_name}")
    print(f"Age: {player.age}")
    print(f"Location: {player.coordinates}")
    print(f"Username: {player.username}")
    print(f"Player: {player}")


if __name__ == "__main__":
    main()
