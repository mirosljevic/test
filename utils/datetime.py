from datetime import datetime, timezone, timedelta
from typing import Optional


def get_current_timestamp() -> str:
    return datetime.now(timezone.utc).isoformat()


def get_tomorrow_timestamp() -> str:
    tomorrow = datetime.now(timezone.utc) + timedelta(days=1)
    return tomorrow.isoformat()


def today_mdy():
    return datetime.now(timezone.utc).strftime("%m/%d/%Y")


def format_duration(seconds: float) -> str:
    if seconds < 60:
        return f"{seconds:.1f}s"

    minutes = int(seconds // 60)
    remaining_seconds = seconds % 60

    if minutes < 60:
        if remaining_seconds > 0:
            return f"{minutes}m {remaining_seconds:.1f}s"
        return f"{minutes}m"

    hours = minutes // 60
    remaining_minutes = minutes % 60

    parts = [f"{hours}h"]
    if remaining_minutes > 0:
        parts.append(f"{remaining_minutes}m")
    if remaining_seconds > 0:
        parts.append(f"{remaining_seconds:.1f}s")

    return " ".join(parts)


def parse_iso_timestamp(timestamp_str: str) -> Optional[datetime]:
    try:
        return datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
    except (ValueError, AttributeError):
        return None
