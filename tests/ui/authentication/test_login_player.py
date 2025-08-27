def test_player_can_login_to_game_web(player):
    player.ui.open()
    player.ui.authentication.login()

    balance = player.ui.account.get_balance()
    name = player.ui.account.get_name()

    assert balance is not None, "Balance should not be None"
    assert name == player.first_name, "Player name should match the logged-in player's name"
