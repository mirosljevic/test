from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from .components.home import GameSection


class InstantsPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Instant Games Page", **kwargs)

    @locate(GameSection)
    def game_section(self) -> GameSection: pass

    def wait_for(self):
        self.page.wait_for_load_state("networkidle")

    def select_game(self, game):
        self.game_section(game).play_now_button.click()
        return self
