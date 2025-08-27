from dataclasses import dataclass
from ui.pages.locator import Selectors


@dataclass
class LoginPageSelectors:
    email_input = Selectors(default="id=username")
    password_input = Selectors(default="id=password")
    forgot_password_link = Selectors()
    sign_in_button = Selectors(default="id=login-button")


@dataclass
class WelcomeMessageSelectors:
    container = Selectors(default="dialog[aria-label='Registration successful dialog']")
    close_button = Selectors(default="button[aria-label='Close registration successful dialog']")
