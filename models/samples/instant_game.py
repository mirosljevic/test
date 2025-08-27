from models import InstantGame, GameType


def main():
    game = InstantGame(
        game_type=GameType.DRAGON_BLAST,
        price=10.0,
        available_bets=[5.0, 10.0],
        configured_for_big_prizes=True,
    )

    print(f"Game: {game}")
    print(f"Name: {game.game_name}")
    print(f"ID: {game.game_id}")


if __name__ == "__main__":
    main()
