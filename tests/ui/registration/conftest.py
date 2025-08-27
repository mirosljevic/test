from pytest import fixture
from actors import PlayerActor
from data_factory import create_player


@fixture(scope="session")
def player(browser, session):
    player_data = create_player()
    player_actor = PlayerActor(player=player_data, browser=browser, session=session)
    return player_actor
