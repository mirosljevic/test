from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from ui.pages.components import Button, Input
from .components import WelcomeMessage
from .components.__selectors__ import LoginPageSelectors as Selectors


class LoginPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Login Page", **kwargs)

    @locate(Input, selector=Selectors.email_input, name="Email Input")
    def email_input(self): pass

    @locate(Input, selector=Selectors.password_input, name="Password Input")
    def password_input(self): pass

    @locate(Button, selector=Selectors.sign_in_button, name="Sign In Button")
    def sign_in_button(self): pass

    @locate(WelcomeMessage)
    def welcome_message(self): pass

    def wait_for(self):
        pass

    def submit_login(self, email, password):
        self.email_input.enter(email)
        self.password_input.enter(password)
        self.sign_in_button.click()

    def close_welcome_message_if_present(self):
        if self.welcome_message.exists():
            self.welcome_message.close_button.click()

