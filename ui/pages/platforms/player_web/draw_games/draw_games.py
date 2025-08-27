from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate

from .components.home import GameSection
from .components.purchase import QuickPick, TicketSelection, PowerPlay, DoublePlay, ShoppingCart, \
    TicketSummary, PurchaseSuccess


class DrawGamesPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Draw Games Page", **kwargs)

    @locate(GameSection)
    def game_section(self): pass

    @locate(QuickPick)
    def quick_pick(self): pass

    @locate(TicketSelection)
    def ticket_selection(self): pass

    @locate(PowerPlay)
    def power_play(self): pass

    @locate(DoublePlay)
    def double_play(self): pass

    @locate(ShoppingCart)
    def shopping_cart(self): pass

    @locate(TicketSummary)
    def ticket_summary(self): pass

    @locate(PurchaseSuccess)
    def purchase_success(self): pass

    def wait_for(self):
        self.page.wait_for_load_state("networkidle")

    def select_game(self, game):
        self.game_section(game).buy_now_button.click()
        return self
