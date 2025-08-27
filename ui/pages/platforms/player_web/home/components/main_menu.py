from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button, DropDown
from ui.pages.locator import locate
from .selectors import MainMenuSelectors as Selectors


class MainMenu(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Main Menu", **kwargs)

    @locate(Button, selector=Selectors.menu_item, component_name="Menu Item Button")
    def item(self): pass

    @locate(DropDown, selector=Selectors.hamburger_button,
            popper=Selectors.mobile_menu_popper, item=Selectors.mobile_menu_item,
            component_name="Mobile Menu")
    def mobile_menu(self): pass

    @property
    def register_button_mobile(self):
        return Button(self.page, selector=Selectors.register_button, component_name="Register Button",
                      instance=self.mobile_menu.popper)

    @property
    def sign_in_button_mobile(self):
        return Button(self.page, selector=Selectors.sign_in_button, component_name="Sign In Button",
                      instance=self.mobile_menu.popper)

    def select(self, item_name: str):
        if self.layout in ["mobile", "tablet"]:
            self.mobile_menu.select(item_name)
        else:
            self.item(item_name).click()

    def select_registration_mobile(self):
        self.mobile_menu.button.click()
        self.register_button_mobile.click()

    def select_sign_in_mobile(self):
        self.mobile_menu.button.click()
        self.sign_in_button_mobile.click()


