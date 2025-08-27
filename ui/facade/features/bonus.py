from ui.pages.platforms.player_web.home import HomePage
from ui.pages.platforms.player_web.bonus import MyBonusesPage


class PlayerBonusUi:
    def __init__(self, page, player=None):
        self.page = page
        self.player = player

        self.home_page = HomePage(self.page)
        self.my_bonuses_page = MyBonusesPage(self.page)

    def go_to_my_bonuses(self):
        self.home_page.wait_for()
        self.home_page.user_controls.user_menu.select("My Bonuses")
        self.my_bonuses_page.select_tab("Bonus Activity")

    def get_latest_bonus(self):
        self.go_to_my_bonuses()
        return self.my_bonuses_page.bonus_card(0).get_details()

