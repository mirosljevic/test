def string_to_float(balance: str) -> float:
    return float(balance.replace("$", "").replace(",", ""))


def string_to_int(number: str) -> int:
    return int(number.replace("$", "").replace(",", ""))