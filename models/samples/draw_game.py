from models import DrawGame, DrawGameType


def main():
    game = DrawGame(
        game_type=DrawGameType.MEGA_MILLIONS,
        ticket_price=2.0,
        draw_id="DRAW_001",
        enabled=True,
    )

    print(f"Game: {game}")
    print(f"Name: {game.game_name}")
    print(f"ID: {game.game_id}")


if __name__ == "__main__":
    main()
