from ui.pages.platforms.player_web.home import HomePage
from ui.pages.platforms.player_web.draw_games import DrawGamesPage, MyTicketsPage
from utils.datetime import today_mdy


class PlayerDrawGamesUi:
    def __init__(self, page, player=None):
        self.page = page
        self.player = player
        self.home_page = HomePage(page)
        self.draw_games_page = DrawGamesPage(page)
        self.my_tickets_page = MyTicketsPage(page)

    def go_to_draw_games(self):
        self.home_page.main_menu.select("Draw Games")
        self.draw_games_page.wait_for()
        return self.draw_games_page

    def go_to_my_tickets(self):
        self.home_page.user_controls.user_menu.select("My Tickets")
        self.my_tickets_page.wait_for()
        return self.my_tickets_page

    def purchase_game(self, game="Powerball", method="quick_pick", plays=3, numbers=[], draws=1,
                      power_play=False, double_play=False):
        self.go_to_draw_games()
        self.draw_games_page.select_game(game)

        if method == "quick_pick":
            self.draw_games_page.quick_pick.quick_pick_button(f"{plays} Plays").click()
        elif method == "select_own":
            self.draw_games_page.quick_pick.quick_pick_button("Create My Own Ticket").click()
            self.draw_games_page.ticket_selection.create_ticket(draws, plays, numbers)
            if game == "Powerball":
                self.draw_games_page.power_play.set(power_play)
                self.draw_games_page.double_play.set(double_play)
        elif method == "repeat":
            self.draw_games_page.quick_pick.quick_pick_button("Same As Last Time").click()
        else:
            raise ValueError(f"Unknown method: {method}")

        self.draw_games_page.shopping_cart.checkout_button(-1).click()
        self.draw_games_page.ticket_summary.complete_button.click()
        self.draw_games_page.purchase_success.close_button.click()

    def filter_tickets(self, date_from=today_mdy(), date_to=today_mdy(), games=None, winning=None, kind="purchase_date"):
        self.go_to_my_tickets()
        self.my_tickets_page.wait_for()
        self.my_tickets_page.filter_tickets_button.click()
        self.my_tickets_page.search_tickets.submit(date_from=date_from, date_to=date_to, games=games,
                                                   winning=winning, kind=kind)

    def get_latest_ticket(self):
        self.go_to_my_tickets()
        self.filter_tickets()
        return self.my_tickets_page.ti

