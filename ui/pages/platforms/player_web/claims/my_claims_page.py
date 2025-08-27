from playwright.sync_api import Page
from ui.pages.base import BasePage
from ui.pages.locator import locate
from .components import ClaimCard, ConfirmClaimDialog, ClaimInfoDialog


class MyClaimsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)

    @locate(ClaimCard)
    def claim_card(self): pass

    @locate(ConfirmClaimDialog)
    def confirm_claim_dialog(self): pass

    @locate(ClaimInfoDialog)
    def claim_info_dialog(self): pass



