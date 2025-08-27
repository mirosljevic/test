from dataclasses import dataclass
from enum import Enum


class OperatorRole(Enum):
    RISK_ANALYST = "Risk Analyst"
    MARKETING_ANALYST = "Marketing Analyst"

    def __str__(self):
        return self.value


@dataclass
class Operator:
    username: str
    password: str
    role: OperatorRole

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"

    @property
    def __dict__(self):
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role.value
        }
