from dataclasses import dataclass
from datetime import datetime, date
from random import randint
from typing import Optional, Tuple


@dataclass
class Player:
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    player_id: Optional[str] = None
    date_of_birth: Optional[datetime] = None
    ssn: Optional[str] = None
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip_code: Optional[str] = None
    country: Optional[str] = None
    phone: Optional[str] = None
    gender: Optional[str] = None
    geolocation: Optional[Tuple[float, float]] = None

    def __str__(self) -> str:
        return f"{self.full_name} ({self.email})"

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

    @property
    def username(self) -> Optional[str]:
        return f"{self.first_name.lower()}_{self.last_name.lower()}_{randint(1000, 9999)}"

    @property
    def age(self) -> Optional[int]:
        if self.date_of_birth is None:
            return None
        today = date.today()
        birth_date = self.date_of_birth.date()
        age = today.year - birth_date.year
        if today.month < birth_date.month or (
            today.month == birth_date.month
            and today.day < birth_date.day
        ):
            age -= 1
        return age

    @property
    def coordinates(self) -> Optional[str]:
        if self.geolocation is None:
            return None
        latitude, longitude = self.geolocation
        lat_dir = "N" if latitude >= 0 else "S"
        lon_dir = "E" if longitude >= 0 else "W"
        return f"{abs(latitude):.6f}°{lat_dir}, {abs(longitude):.6f}°{lon_dir}"

    @property
    def longitude(self) -> Optional[float]:
        return self.geolocation[1] if self.geolocation else None

    @property
    def latitude(self) -> Optional[float]:
        return self.geolocation[0] if self.geolocation else None

    @property
    def ssn_last_four(self) -> Optional[str]:
        if self.ssn:
            return self.ssn[-4:]
        return None
