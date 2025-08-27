from models import Bonus, BonusType


def main():
    bonus = Bonus(
        bonus_type=BonusType.FREE_ROUNDS,
    )

    print(f"Bonus: {bonus}")
    print(f"Type: {bonus.bonus_type}")


if __name__ == "__main__":
    main()
