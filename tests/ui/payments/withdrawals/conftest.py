from pytest import fixture
from actors import PlayerActor, OperatorActor


@fixture(scope="session")
def player(browser, mongo, session):
    available_player = mongo.get_available_player(type="winner")
    available_player.lock()
    player = PlayerActor(player=available_player.player, browser=browser, session=session)
    yield player
    available_player.set_used()


@fixture(scope="session")
def risk_analyst(mongo, session):
    available_analyst = mongo.get_available_operator(role="Risk Analyst")
    available_analyst.lock()
    analyst = OperatorActor(operator=available_analyst.operator, session=session)
    analyst.authenticate()
    yield analyst
    available_analyst.set_available()