from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button, Input
from ui.pages.locator import locate
from .__selectors__ import PasswordSelectors as Selectors


class PasswordDetails(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Password Details", **kwargs)

    @locate(Button, selector=Selectors.edit_button, name="Edit Password Button")
    def edit_button(self) -> Button: pass

    @locate(Input, selector=Selectors.current_password_input, name="Current Password Input")
    def current_password_input(self) -> Input: pass

    @locate(Input, selector=Selectors.new_password_input, name="New Password Input")
    def new_password_input(self) -> Input: pass

    @locate(Input, selector=Selectors.confirm_password_input, name="Confirm Password Input")
    def confirm_password_input(self) -> Input: pass

    @locate(Button, selector=Selectors.save_button, name="Save Password Button")
    def save_button(self) -> Button: pass

    def edit_password(self, current_password: str, new_password: str):
        self.edit_button().click()
        self.current_password_input().enter(current_password)
        self.new_password_input().enter(new_password)
        self.confirm_password_input().enter(new_password)
        self.save_button().click()
        return self
