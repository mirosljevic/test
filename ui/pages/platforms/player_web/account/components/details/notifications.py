from datetime import datetime
from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Checkbox
from ui.pages.locator import locate
from .__selectors__ import NotificationSelectors as Selectors


class NotificationDetails(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Notification Details", **kwargs)

    @locate(Checkbox, selector=Selectors.checkboxes, name="Notification Checkbox")
    def notification_checkbox(self) -> Checkbox: pass

    @property
    def offers_checkbox(self) -> Checkbox:
        return self.notification_checkbox("personalized email offers")

    @property
    def winning_numbers_checkbox(self) -> Checkbox:
        return self.notification_checkbox("winning numbers")




