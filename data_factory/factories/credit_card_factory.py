from typing import Optional
from faker import Faker
from models import CreditCard
from logger import log

faker = Faker("en_US")


def create_credit_card(card_type: Optional[str] = None, cardholder: Optional[str] = None, **kwargs) -> CreditCard:
    card_type_mapping = {
        "visa": "visa",
        "mastercard": "mastercard",
        "amex": "amex",
        "discover": "discover",
    }
    if card_type and card_type.lower() in card_type_mapping:
        faker_card_type = card_type_mapping[card_type.lower()]
        card_number = faker.credit_card_number(card_type=faker_card_type)
        log.debug(f"Generating {card_type} card")
    else:
        card_number = faker.credit_card_number()
        log.debug("Generating random card type")

    if card_number.startswith(("34", "37")):
        cvv = faker.random_number(digits=4, fix_len=True)
    else:
        cvv = faker.random_number(digits=3, fix_len=True)
    clean_number = card_number.replace(" ", "").replace("-", "")
    if len(clean_number) not in [15, 16]:
        card_number = faker.credit_card_number(card_type="visa")
        log.debug(f"Regenerated card due to invalid length: ****{card_number[-4:]}")
    card_data = {
        "number": card_number,
        "expiry_month": faker.month(),
        "expiry_year": faker.random.choice(["2028", "2029", "2030", "2031", "2032"]),
        "cvv": str(cvv),
        "cardholder_name": cardholder,
    }
    if card_type:
        card_data["card_type"] = card_type.lower()
    card_data.update(kwargs)
    card = CreditCard(**card_data)
    log.debug(f"Successfully generated credit card: {card}")
    return card
