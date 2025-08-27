import re


def sanitize_filename(filename: str) -> str:
    sanitized = re.sub(r'[<>:"/\\|?*]', "_", filename)
    sanitized = sanitized.strip(" .")
    return sanitized if sanitized else "unnamed"


def truncate_string(text: str, max_length: int, suffix: str = "...") -> str:
    if len(text) <= max_length:
        return text

    if len(suffix) >= max_length:
        return text[:max_length]

    return text[: max_length - len(suffix)] + suffix


def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split("_")
    return components[0] + "".join(word.capitalize() for word in components[1:])


def camel_to_snake(camel_str: str) -> str:
    snake_str = re.sub("([a-z0-9])([A-Z])", r"\1_\2", camel_str)
    return snake_str.lower()
