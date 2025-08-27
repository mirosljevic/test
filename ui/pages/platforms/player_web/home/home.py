from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from .components import MainMenu, UserControls


class HomePage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Home Page", **kwargs)

    @locate(MainMenu)
    def main_menu(self): pass

    @locate(UserControls)
    def user_controls(self): pass

    def wait_for(self):
        pass

    def start_registration(self):
        if self.layout in ["mobile", "tablet"]:
            self.main_menu.select_registration_mobile()
        else:
            self.user_controls.register_button.click()

    def start_authentication(self):
        if self.layout in ["mobile", "tablet"]:
            self.main_menu.select_sign_in_mobile()
        else:
            self.user_controls.sign_in_button.click()

    def get_account_balance(self):
        return self.user_controls.get_balance()


