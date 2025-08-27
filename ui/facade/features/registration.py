from ui.pages.platforms.player_web.home import HomePage
from ui.pages.platforms.player_web.registration import RegistrationPage
from email_service import EmailClient


class PlayerRegistrationUi:
    def __init__(self, page, player=None, email=None):
        self.page = page
        self.player = player
        self.home_page = HomePage(page)
        self.registration_page = RegistrationPage(page)
        self.email = email or EmailClient(self.player.username)

    def go_to_registration(self):
        self.home_page.wait_for()
        self.home_page.start_registration()

    def submit_registration(self):
        self.registration_page.wait_for()
        self.player.email = self.email.create_account()

        self.registration_page.registration_init.submit(self.player.email)
        self.registration_page.verify_email.wait_for()

        request_id, token, link = self.email.get_registration_auth_details()
        self.page.goto(link)
        self.registration_page.create_account.submit_registration(self.player)
        self.registration_page.welcome_dialog.close_button.click()
        return self.player

    def go_to_login(self):
        pass

    def submit_login(self):
        pass

