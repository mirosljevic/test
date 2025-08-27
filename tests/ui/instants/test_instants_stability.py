from pytest import mark
from models import InstantGames

GAME = InstantGames.lucky_forest
ROUNDS = 1
BET = 1


@mark.stability
@mark.instants
def test_instants_stability():
    pass
