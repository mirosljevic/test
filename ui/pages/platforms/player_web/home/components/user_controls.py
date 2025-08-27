from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button, Text, DropDown
from ui.pages.locator import locate
from utils.currency import string_to_float, string_to_int
from .selectors import UserControlSelectors as Selectors


class UserControls(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="User Controls", **kwargs)

    @locate(Button, selector=Selectors.register_button, component_name="Register Button")
    def register_button(self): pass

    @locate(Button, selector=Selectors.sign_in_button, component_name="Sign In Button")
    def sign_in_button(self): pass

    @locate(Text, selector=Selectors.balance_label, component_name="Balance Label")
    def balance_label(self): pass

    @property
    def balance_label_mobile(self):
        return Text(self.page, selector=Selectors.balance_label_mobile, component_name="Balance Mobile Label",
                    instance=self.user_menu.popper, index=1)

    @locate(Text, selector=Selectors.points_label, component_name="Points Label")
    def points_label(self): pass

    @property
    def points_label_mobile(self):
        return Text(self.page, selector=Selectors.points_label_mobile, component_name="Points Mobile Label",
                    instance=self.user_menu.popper, index=2)

    @locate(Text, selector=Selectors.points_label_mobile, component_name="Points Mobile Label")
    def points_label_mobile(self): pass

    @locate(Text, selector=Selectors.first_name_label, component_name="First Name Label")
    def first_name_label(self): pass

    @locate(DropDown, selector=Selectors.user_menu_button, popper=Selectors.user_menu_popper,
            item=Selectors.user_menu_item, component_name="User Menu")
    def user_menu(self): pass

    def get_balance(self):
        if self.layout in ["mobile", "tablet"]:
            self.user_menu.button.click()
            return string_to_float(self.balance_label_mobile.get_text())
        else:
            return string_to_float(self.balance_label.get_text())

    def get_points(self):
        return string_to_int(self.points_label.text_content())

    def get_first_name(self):
        return self.first_name_label.text_content().strip()