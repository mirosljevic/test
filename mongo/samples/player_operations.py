from mongo.player_client import PlayerClient
from logger import log as logger


def main():
    logger.info("=== Player Operations Sample ===")

    try:
        # Get an available player
        player = PlayerClient.get_available_player(
            {"is_verified": True},
            host="localhost",
            port=27017,
            database="test_db"
        )

        if player:
            logger.info(f"✅ Locked player: {player.player_id}")
            logger.info(f"Player data: {player.get_player_data()}")

            # Update player
            player.update_player({"last_login": "2024-07-15T10:30:00Z"})
            logger.info("✅ Player updated")

            # Unlock player
            player.unlock_player()
            logger.info("✅ Player unlocked")

        else:
            logger.info("❌ No available players found")

    except Exception as e:
        logger.error(f"Error: {e}")

    finally:
        logger.info("Player operations completed")


if __name__ == "__main__":
    main()
