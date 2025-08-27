from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button, Input
from ui.pages.locator import locate
from .selectors import RegistrationInitSelectors as Selectors


class RegistrationInit(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Registration Init Modal", **kwargs)

    @locate(Input, selector=Selectors.email_field, component_name="Email Field")
    def email_field(self): pass

    @locate(Button, selector=Selectors.continue_button, component_name="Continue Button")
    def continue_button(self): pass

    def submit(self, email: str):
        self.email_field.enter(email)
        self.continue_button.click()

    def wait_for(self):
        pass
