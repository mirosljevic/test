import os
from typing import Any


def get_config_var(name: str, default: Any) -> Any:
    env_value = os.environ.get(name)
    if env_value is None:
        return default

    if isinstance(default, bool):
        return env_value.lower() in ("true", "1", "yes", "on")

    if isinstance(default, int):
        try:
            return int(env_value)
        except ValueError:
            return default

    if isinstance(default, float):
        try:
            return float(env_value)
        except ValueError:
            return default

    return env_value
