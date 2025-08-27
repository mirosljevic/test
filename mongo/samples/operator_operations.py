from mongo.operator_client import OperatorClient
from logger import log as logger


def main():
    logger.info("=== Operator Operations Sample ===")

    try:
        # Get an available operator
        operator = OperatorClient.get_available_operator(
            {"role": "admin"},
            host="localhost",
            port=27017,
            database="test_db"
        )

        if operator:
            logger.info(f"✅ Locked operator: {operator.operator_id}")
            logger.info(f"Operator data: {operator.get_operator_data()}")

            # Update operator
            operator.update_operator({"last_login": "2024-07-15T10:30:00Z"})
            logger.info("✅ Operator updated")

            # Unlock operator
            operator.unlock_operator()
            logger.info("✅ Operator unlocked")

        else:
            logger.info("❌ No available operators found")

    except Exception as e:
        logger.error(f"Error: {e}")

    finally:
        logger.info("Operator operations completed")


if __name__ == "__main__":
    main()
