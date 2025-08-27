from pytest import mark
from datetime import datetime

GAME = "Powerball"
NUMBERS = [[12, 17, 20, 22, 46, 25], [4, 5, 10, 22, 23, 6], [5, 8, 9, 21, 22, 26]]
DRAWS = 3


@mark.stability
def test_stability_dgs(player):
    player.ui.open()
    player.ui.authentication.login()

    balance = player.ui.account.get_balance()
    player.ui.dgs.purchase_game(game=GAME, method="select_own", plays=len(NUMBERS), numbers=NUMBERS, draws=DRAWS)

    ticket = player.ui.dgs.get_ticket()
