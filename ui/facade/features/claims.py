from ui.pages.platforms.player_web.home import HomePage
from ui.pages.platforms.player_web.account import MyAccountPage
from ui.pages.platforms.player_web.claims import MyClaimsPage


class PlayerClaimsUi:
    def __init__(self, page, player=None):
        self.page = page
        self.player = player

        self.home_page = HomePage(self.page)
        self.my_account_page = MyAccountPage(self.page)
        self.my_claims_page = MyClaimsPage(self.page)

    def go_to_my_claims(self):
        self.home_page.user_controls.user_menu.select("My Account")
        self.my_account_page.my_account_menu.select("My Claims")
        return self.my_claims_page

    def claim_latest_item(self):
        self.go_to_my_claims()
        self.my_claims_page.claim_card(0).claim_button.click()
        self.my_claims_page.confirm_claim_dialog.submit_button.click()
        self.my_claims_page.claim_info_dialog.close_button.click()
        return self

    def get_latest_claim(self):
        self.go_to_my_claims()
        return self.my_claims_page.claim_card(0).get_details()
