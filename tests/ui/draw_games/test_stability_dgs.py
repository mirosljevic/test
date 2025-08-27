from pytest import mark
from datetime import datetime

GAME = "Powerball"
NUMBERS = [[12, 17, 20, 22, 46, 25], [4, 5, 10, 22, 23, 6], [5, 8, 9, 21, 22, 26]]
DRAWS = 3


@mark.stability
@mark.dgs
def test_stability_dgs():
    pass
