from models import CreditCard


def main():
    card = CreditCard(
        number="4111 1111 1111 1111",
        expiry_month="12",
        expiry_year="2025",
        cvv="123",
        cardholder_name="John Doe",
    )

    print(f"Card: {card}")
    print(f"Expiry Full Year: {card.expiry_full_year}")
    print(f"Expiry Short Year: {card.expiry_short_year}")


if __name__ == "__main__":
    main()
