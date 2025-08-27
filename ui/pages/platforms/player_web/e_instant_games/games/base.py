from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.components import CanvasButton, Text, Button
from ui.pages.locator import locate
from logger import log
from .__selectors__ import BaseGameSelectors as Selectors


class BaseGame(BasePage):
    def __init__(self, page: Page, coordinates=None, **kwargs):
        super().__init__(page=page, **kwargs)
        self.page = page
        self.coordinates = coordinates
        self.frame_locator = "iframe#ngl-rgs-game-container"

    @locate(CanvasButton, button="continue", component_name="Continue Button")
    def continue_button(self) -> CanvasButton: pass

    @locate(CanvasButton, button="play", component_name="Play Button")
    def play_button(self) -> CanvasButton: pass

    @locate(CanvasButton, button="cost_plus", component_name="Cost Plus Button")
    def cost_plus_button(self) -> CanvasButton: pass

    @locate(CanvasButton, button="cost_minus", component_name="Cost Minus Button")
    def cost_minus_button(self) -> CanvasButton: pass

    @locate(CanvasButton, button="reveal_all", component_name="Reveal All Button")
    def reveal_all_button(self) -> CanvasButton: pass

    @locate(CanvasButton, button="play_again", component_name="Play Again Button")
    def play_again_button(self) -> CanvasButton: pass

    @locate(CanvasButton, button="close", component_name="Close Button")
    def close_button(self) -> CanvasButton: pass

    @locate(Text, selector=Selectors.labels, component_name="Balance Label", index=0, in_frame=True)
    def balance_label(self) -> Text: pass

    @locate(Text, selector=Selectors.labels, component_name="Total Cost Label", index=1, in_frame=True)
    def total_cost_label(self) -> Text: pass

    @locate(Text, selector=Selectors.labels, component_name="Total Winnings Label", index=2, in_frame=True)
    def total_winnings_label(self) -> Text: pass

    @locate(Button, selector=Selectors.confirm_close_button, component_name="Confirm Close Button")
    def confirm_close_button(self) -> Button: pass

    @locate(Button, selector=Selectors.bonus_play_button, component_name="Bonus Let's Play Button")
    def bonus_play_button(self) -> Button: pass

    @locate(Button, selector=Selectors.bonus_close_button, component_name="Bonus Close Button")
    def bonus_close_button(self) -> Button: pass

    def get_balance(self):
        return float(self.balance_label.get_text().replace("$", "").replace(",", "").strip())

    def get_total_cost(self):
        return float(self.total_cost_label.get_text().replace("$", "").replace(",", "").strip())

    def get_total_winnings(self):
        return float(self.total_winnings_label.get_text().replace("$", "").replace(",", "").strip())

    def select_cost(self, total_cost=None):
        if total_cost is not None:
            while self.get_total_cost() != total_cost:
                if self.get_total_cost() < total_cost:
                    self.cost_plus_button.click()
                elif self.get_total_cost() > total_cost:
                    self.cost_minus_button.click()

    def play(self, plays=1, ticket_cost=None, bonus=False, **kwargs):
        if bonus:
            self.bonus_play_button.click()
        if self.continue_button.is_displayed():
            self.continue_button.click()
        self.select_cost(ticket_cost)
        for _ in range(plays):
            self.play_button.click()
            self.reveal_all_button.click()
            if bonus and _ == plays - 2:
                self.bonus_play_button.click()
            self.play_again_button.wait_for()
            log.info(f"Play #{_ + 1} completed with ticket cost: {ticket_cost} and winnings: {self.get_total_winnings()}")

        self.close_button.click()
        self.confirm_close_button.click()
        return True

