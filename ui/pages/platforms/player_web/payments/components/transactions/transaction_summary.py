from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Text, Button
from ui.pages.locator import locate
from .__selectors__ import TransactionSummarySelectors as Selectors


class TransactionSummary(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Transaction Summary", **kwargs)

    @locate(Text, selector=Selectors.item, component_name="Item")
    def item(self) -> Text: pass

    @locate(Button, selector=Selectors.close_button, component_name="Close Button")
    def close_button(self) -> Button: pass

    def get_item_value(self, item):
        return (self.item.locator.locator(f".wc-justify-between:has-text('{item}')")
                .locator(".wc-font-semibold").inner_text())
