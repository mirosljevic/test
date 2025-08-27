from pytest import mark
from models import InstantGames

GAME = InstantGames.lucky_forest
ROUNDS = 1
BET = 1


@mark.stability
def test_instants_stability(player):
    player.ui.open()
    player.ui.authentication.login()

    initial_balance = player.ui.account.get_balance()
    player.ui.instants.play_game(game=GAME, rounds=ROUNDS)

    play_details = player.ui.instants.get_play(game=GAME)
    balance = player.ui.account.get_balance()

    assert abs(play_details["play"]) == BET
    assert balance == initial_balance + play_details["play"] + play_details["win"]


