from ui.pages.platforms.player_web.home import HomePage
from ui.pages.platforms.player_web.authentication import LoginPage


class PlayerAuthenticationUi:
    def __init__(self, page, player=None):
        self.page = page
        self.player = player
        self.home_page = HomePage(page)
        self.login_page = LoginPage(page)

    def go_to_login(self):
        self.home_page.wait_for()
        self.home_page.start_authentication()
        return self.login_page

    def login(self, email=None, password=None, retry_attempts=1):
        self.go_to_login()
        for _ in range(retry_attempts):
            self.login_page.submit_login(
                email=email or self.player.email,
                password=password or self.player.password,
            )
        self.login_page.close_welcome_message_if_present()


