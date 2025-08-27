from typing import List, Optional
import random
from faker import Faker
from models import BankAccount
from logger import log

faker = Faker("en_US")
VALID_ROUTING_NUMBERS = [
    "121000248",
    "111000025",
    "026009593",
    "021000021",
    "122105155",
    "071000013",
    "051000017",
    "061000104",
    "121042882",
    "054001204",
]


def create_bank_account(
    account_type: Optional[str] = None, include_optional_fields: bool = True, **kwargs
) -> BankAccount:
    log.debug("Generating bank account")
    account_number = faker.random_number(digits=random.randint(10, 15), fix_len=True)
    account_number_str = str(account_number)
    routing_number = random.choice(VALID_ROUTING_NUMBERS)
    account_data = {
        "account_number": account_number_str,
        "routing_number": routing_number,
    }
    if include_optional_fields:
        if account_type and account_type.lower() in ["checking", "savings"]:
            acc_type = account_type.lower()
        else:
            acc_type = random.choice(["checking", "savings"])
        account_holder_name = faker.name()
        account_data.update(
            {
                "account_type": acc_type,
                "account_holder_name": account_holder_name,
            }
        )
        log.debug(f"Generated {acc_type} account for {account_holder_name}")
    account_data.update(kwargs)
    log.debug(f"Successfully generated bank account: ****{account_number_str[-4:]}")
    return BankAccount(**account_data)


def create_bank_accounts(
    count: int,
    account_types: Optional[List[str]] = None,
    include_optional_fields: bool = True,
    **kwargs,
) -> List[BankAccount]:
    log.debug(f"Generating {count} bank accounts")
    accounts = []
    for i in range(count):
        try:
            account_type = None
            if account_types:
                account_type = random.choice(account_types)
            account = create_bank_account(
                account_type=account_type,
                include_optional_fields=include_optional_fields,
                **kwargs,
            )
            accounts.append(account)
        except Exception as e:
            log.warning(f"Failed to generate bank account {i+1}: {e}")
            continue
    log.debug(
        f"Successfully generated {len(accounts)} out of {count} requested bank accounts"
    )
    return accounts


def create_test_account_set() -> List[BankAccount]:
    log.debug("Generating test account set")
    test_accounts = [
        create_bank_account(account_type="checking"),
        create_bank_account(account_type="checking"),
        create_bank_account(account_type="savings"),
        create_bank_account(account_type="savings"),
        create_bank_account(include_optional_fields=False),
        create_bank_account(include_optional_fields=False),
    ]
    log.debug(f"Generated {len(test_accounts)} test accounts")
    return test_accounts
