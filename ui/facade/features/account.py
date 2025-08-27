from time import sleep
from ui.pages.platforms.player_web.home import HomePage
from ui.pages.platforms.player_web.account import MyAccountPage, MyDetailsPage


class PlayerAccountUi:
    def __init__(self, page, player=None):
        self.page = page
        self.player = player
        self.home_page = HomePage(page)
        self.my_account_page = MyAccountPage(page)
        self.my_details_page = MyDetailsPage(page)

    def get_balance(self, wait=0):
        sleep(wait)
        return self.home_page.user_controls.get_balance()

    def get_points(self):
        return self.home_page.user_controls.get_points()

    def go_to_my_account(self):
        self.home_page.user_controls.user_menu.select("My Account")
        return self.my_account_page

    def get_account_profile(self):
        self.go_to_my_account()
        self.my_account_page.my_account_menu.select("My Details")
        return self.my_details_page.get_profile()



