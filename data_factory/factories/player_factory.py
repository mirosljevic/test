import random
from datetime import date, datetime, timedelta
from faker import Faker
from models import Player
from environment import settings
from logger import log

_kansas_faker = Faker("en_US")
_default_faker = Faker("en_US")


def _get_kansas_address_data():
    kansas_cities = [
        ("Wichita", "67202", 37.6872, -97.3301),
        ("Overland Park", "66204", 38.9822, -94.6708),
        ("Kansas City", "66101", 39.1142, -94.6275),
        ("Topeka", "66601", 39.0473, -95.6890),
        ("Olathe", "66061", 38.8814, -94.8191),
        ("Lawrence", "66044", 38.9717, -95.2353),
        ("Shawnee", "66216", 39.0228, -94.7202),
        ("Manhattan", "66502", 39.1836, -96.5717),
        ("Lenexa", "66219", 38.9536, -94.7336),
        ("Salina", "67401", 38.8403, -97.6114),
        ("Hutchinson", "67501", 38.0608, -97.9298),
        ("Leavenworth", "66048", 39.3111, -94.9222),
        ("Leawood", "66206", 38.9667, -94.6169),
        ("Dodge City", "67801", 37.7528, -100.0171),
        ("Garden City", "67846", 37.9717, -100.8727),
    ]
    city_data = random.choice(kansas_cities)
    city, zip_code, latitude, longitude = city_data
    return city, "KS", zip_code, latitude, longitude


def _get_kansas_phone_number():
    kansas_area_codes = ["316", "620", "785", "913"]
    area_code = random.choice(kansas_area_codes)
    number = f"{random.randint(200, 999)}{random.randint(1000, 9999)}"
    return f"{area_code}{number}"


def create_player(include_optional_fields: bool = True, **kwargs) -> Player:
    tenant = settings.tenant
    log.debug(f"Generating player for tenant: {tenant}")
    if tenant == "Kansas":
        faker = _kansas_faker
    else:
        faker = _default_faker

    is_male = faker.boolean()
    first_name = faker.first_name_male() if is_male else faker.first_name_female()
    last_name = faker.last_name()

    min_age, max_age = 18, 75
    today = date.today()
    max_birth_date = today - timedelta(days=min_age * 365)
    min_birth_date = today - timedelta(days=max_age * 365)
    birth_date = faker.date_between(start_date=min_birth_date, end_date=max_birth_date)
    birth_datetime = datetime.combine(birth_date, datetime.min.time())

    email = f"{first_name.lower()}.{last_name.lower()}@{faker.domain_name()}"
    ssn = faker.ssn().replace("-", "")
    player_data = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "date_of_birth": birth_datetime,
        "ssn": ssn
    }
    if include_optional_fields:
        if tenant == "Kansas":
            city, state, zip_code, latitude, longitude = _get_kansas_address_data()
            phone = _get_kansas_phone_number()
        else:
            city, state, zip_code, latitude, longitude = _get_kansas_address_data()
            phone = _get_kansas_phone_number()
        player_data.update(
            {
                "address": f"{faker.street_address()}",
                "city": city,
                "state": state,
                "zip_code": zip_code,
                "phone": phone,
                "password": faker.password(
                    length=12,
                    special_chars=True,
                    digits=True,
                    upper_case=True,
                    lower_case=True,
                ),
                "country": "US",
                "gender": "Male" if is_male else "Female",
                "geolocation": (latitude, longitude),
            }
        )
    player_data.update(kwargs)
    player = Player(**player_data)
    log.debug(f"Successfully generated player: {player}")
    return player
