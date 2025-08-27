from playwright.sync_api import Page
from ui.pages.components import BaseComponent, Button
from ui.pages.locator import locate
from .__selectors__ import TicketSelectionSelectors as Selectors

from .number_selection import NumberSelection
from .draw_selection import DrawSelection
from .play_selection import PlaySelection
from .ticket_row import TicketRow


class TicketSelection(BaseComponent):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, selector=Selectors.container, component_name="Ticket Selection", **kwargs)

    @locate(NumberSelection)
    def number_selection(self): pass

    @locate(DrawSelection)
    def draw_selection(self): pass

    @locate(PlaySelection)
    def play_selection(self): pass

    @locate(TicketRow)
    def ticket_row(self): pass

    @locate(Button, selector=Selectors.continue_button, component_name="Continue Button")
    def continue_button(self): pass

    def select_draws(self, value: int):
        self.draw_selection.select(value)
        return self

    def select_plays(self, value: int):
        self.play_selection.select(value)
        return self

    def select_numbers(self, *numbers):
        for index, row_numbers in enumerate(numbers):
            self.ticket_row(index).primary_number_button(0).click()
            self.number_selection.select_numbers(*row_numbers)
        return self

    def create_ticket(self, draws, plays, numbers):
        self.select_draws(draws).select_plays(plays).select_numbers(*numbers)
        self.continue_button.click()


