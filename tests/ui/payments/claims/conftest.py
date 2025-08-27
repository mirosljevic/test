from pytest import fixture
from actors import PlayerActor, OperatorActor


@fixture(scope="session")
def player(browser, mongo, session):
    available_player = mongo.get_available_player(type="high_value_winner")
    available_player.lock()
    player = PlayerActor(player=available_player.player, browser=browser, session=session)
    yield player
    available_player.set_used()


@fixture(scope="function")
def risk_manager(mongo):
    available_risk_manager = mongo.get_available_operator(role="Risk Manager")
    available_risk_manager.lock()
    risk_manager = OperatorActor(operator=available_risk_manager.operator)
    yield risk_manager
    available_risk_manager.set_available()

