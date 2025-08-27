from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button, Text
from ui.pages.locator import locate
from .__selectors__ import PlaySummarySelectors as Selectors
from utils.currency import string_to_float


class PlaySummary(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Play Summary Dialog", **kwargs)

    @locate(Button, selector=Selectors.close_button, component_name="Close Button")
    def close_button(self): pass

    @locate(Text, selector=Selectors.play_text, component_name="Play Text")
    def play_text(self): pass

    @locate(Text, selector=Selectors.win_text, component_name="Win Text")
    def win_text(self): pass

    @locate(Text, selector=Selectors.ticket_id_text, component_name="Ticket ID Text")
    def ticket_id_text(self): pass

    def get_details(self):
        return {
            "play": string_to_float(self.play_text.get_text()),
            "win": string_to_float(self.win_text.get_text()),
            "ticket_id": self.ticket_id_text.get_text()
        }
