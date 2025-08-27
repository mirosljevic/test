from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text, Button
from ui.pages.locator import locate
from .selectors import WelcomeDialogSelectors as Selectors


class WelcomeDialog(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Welcome Dialog", **kwargs)

    @locate(Text, selector=Selectors.welcome_text, component_name="Welcome Text")
    def welcome_text(self): pass

    @locate(Text, selector=Selectors.sign_in_button, component_name="Sign In Button")
    def sign_in_button(self): pass

    @locate(Button, selector=Selectors.close_button, component_name="Close Button")
    def close_button(self): pass
