from pytest import fixture
from actors import PlayerActor


@fixture(scope="session")
def player(browser, mongo, session):
    available_player = mongo.get_available_player(type="verified_player")
    available_player.lock()
    player = PlayerActor(player=available_player.player, browser=browser, session=session)
    yield player
    available_player.set_used()
