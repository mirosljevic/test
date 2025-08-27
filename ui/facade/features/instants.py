from models import InstantGame
from ui.pages.platforms.player_web.home import HomePage
from ui.pages.platforms.player_web.e_instant_games import InstantsPage, Game, PlayHistoryPage
from ui.pages.platforms.player_web.account import MyAccountPage


class PlayerInstantsUi:
    def __init__(self, page, player=None):
        self.page = page
        self.player = player

        self.home_page = HomePage(page)
        self.instants_page = InstantsPage(page)
        self.my_account_page = MyAccountPage(page)
        self.game = lambda game_name: Game(game_name, page)
        self.play_history_page = PlayHistoryPage(page)

    def go_to_instants(self):
        self.home_page.main_menu.select("eInstant Games")
        self.instants_page.wait_for()
        return self.instants_page

    def play_game(self, game: InstantGame, rounds=1, ticket_cost=None, ticket_number=None, bonus=False):
        self.go_to_instants()
        self.page.wait_for_load_state("networkidle")
        self.instants_page.select_game(game.name)
        self.game(game.name).play(plays=rounds, ticket_cost=ticket_cost, ticket_number=ticket_number, bonus=bonus)

    def play_demo(self, game, plays=1, ticket_cost=None, ticket_number=None):
        self.go_to_instants()
        self.instants_page.select_demo(game)
        self.game.play(plays=plays, ticket_cost=ticket_cost, ticket_number=ticket_number)

    def go_to_instants_history(self):
        self.home_page.user_controls.user_menu.select("My Account")
        self.my_account_page.my_account_menu.select("eInstant Play History")

    def get_play(self, **kwargs):
        self.go_to_instants_history()
        return self.play_history_page.get_latest_play(**kwargs)

