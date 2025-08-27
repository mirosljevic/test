from playwright.sync_api import Page
from ui.pages import BasePage
from ui.pages.locator import locate
from .components.history import HistoryItem, PlaySummary


class PlayHistoryPage(BasePage):
    def __init__(self, page: Page, **kwargs):
        super().__init__(page, page_name="Instant Play History", **kwargs)

    @locate(HistoryItem)
    def history_item(self) -> HistoryItem: pass

    @locate(PlaySummary)
    def play_summary(self) -> PlaySummary: pass

    def get_latest_play(self, **kwargs):
        self.history_item(-1).view_button.click()
        details = self.play_summary.get_details()
        self.play_summary.close_button.click()
        return details




