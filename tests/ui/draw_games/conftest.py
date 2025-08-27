from pytest import fixture
from actors import PlayerActor
from models import Player


@fixture(scope="session")
def player(browser, mongo, session):
    available_player = mongo.get_available_player(type="depositor")
    available_player.lock()
    player = PlayerActor(player=available_player.player, browser=browser, session=session)
    yield player
    available_player.set_used()


@fixture(scope="session")
def hardcoded_player(browser, session):
    player = Player(email="robert_collins_250731@pollardteam965267.testinator.com",
                    password="Pa$$w0rd!", player_id="2012662")
    player = PlayerActor(player=player, browser=browser, session=session)
    yield player
