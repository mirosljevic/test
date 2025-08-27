from pytest import mark

RETRY_ATTEMPTS = 5


@mark.stability
def test_failed_login_stability(player):
    player.ui.open()
    player.ui.authentication.login(password="wrong_password", retry_attempts=RETRY_ATTEMPTS)
    player.ui.close()

    player.ui.open()
    player.ui.authentication.login()
    print()
