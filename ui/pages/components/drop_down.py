from playwright.sync_api import Page
from .base import BaseComponent
from .button import Button
from logger import log


class DropDown(BaseComponent):
    def __init__(self, page: Page, selector, popper=None, item=None, **kwargs):
        super().__init__(page=page, selector=selector, **kwargs)
        self._button = selector
        self._popper = popper
        self._item = item

    @property
    def button(self):
        return Button(self.page,
                      component_name="Drop Down Button",
                      instance=self)

    @property
    def popper(self):
        return BaseComponent(self.page,
                             selector=self._popper,
                             component_name="Drop Down Popper",
                             instance=None)

    def item(self, value):
        return Button(self.page, selector=self._item,
                      component_name="Drop Down Item",
                      instance=self.popper, value=value)

    def select(self, value):
        self.button.click()
        self.popper.wait_for()
        self.item(value).click()

    def click(self):
        self.button.click()
