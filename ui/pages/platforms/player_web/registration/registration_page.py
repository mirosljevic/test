from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from .components import RegistrationInit, VerifyEmail, CreateAccount, WelcomeDialog


class RegistrationPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Registration Page", **kwargs)

    @locate(RegistrationInit)
    def registration_init(self): pass

    @locate(VerifyEmail)
    def verify_email(self): pass

    @locate(CreateAccount)
    def create_account(self): pass

    @locate(WelcomeDialog)
    def welcome_dialog(self): pass

    def wait_for(self):
        pass


