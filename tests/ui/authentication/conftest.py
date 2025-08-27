from pytest import fixture
from models import Player
from actors.player import PlayerActor


@fixture(scope="session")
def player(browser):
    player = Player(email="qa.automation.pds.1721805985919@gmail.com", password="Pa$$w0rd!", first_name="Sharon")
    return PlayerActor(player=player, browser=browser)
