from pytest import fixture
from actors import PlayerActor, OperatorActor
from models import Player
from uuid import uuid4

FREE_ROUNDS_NAME = "Free Rounds AUTOMATED"
FREE_ROUNDS_GAMES = ["LF"]
FREE_ROUNDS_COST_PER_TICKET = 1
FREE_ROUNDS_NUMBER_OF_ROUNDS = 3
FREE_ROUNDS_NUMBER_OF_TICKETS = 1


@fixture(scope="session")
def hardcoded_player(browser, session):
    player = Player(email="megan_russell_5022@pollardteam965267.testinator.com",
                    password="@_8HgydB(bpF", player_id="193833", geolocation=(37.6872, -97.3301))
    player = PlayerActor(player=player, browser=browser, session=session)
    player.authenticate()
    return player


@fixture(scope="session")
def player(browser, mongo, session):
    available_player = mongo.get_available_player(type="bonus_player")
    available_player.lock()
    player = PlayerActor(player=available_player.player, browser=browser, session=session)
    yield player
    available_player.set_used()


@fixture(scope="session")
def marketing_analyst(mongo, session):
    marketing_analyst = mongo.get_available_operator(role="Marketing Analyst")
    marketing_analyst.lock()
    operator = OperatorActor(operator=marketing_analyst.operator, session=session)
    operator.authenticate()
    yield operator
    marketing_analyst.set_available()


@fixture(scope="session")
def free_rounds_bonus(marketing_analyst):
    bonus_object = marketing_analyst.api.bonus.get_bonus_object(name=FREE_ROUNDS_NAME)
    if not bonus_object:
        bonus_object = marketing_analyst.api.bonus.create_free_rounds_object(
            games=FREE_ROUNDS_GAMES,
            cost_per_ticket=FREE_ROUNDS_COST_PER_TICKET,
            object_name=FREE_ROUNDS_NAME,
            number_of_rounds=FREE_ROUNDS_NUMBER_OF_ROUNDS,
            number_of_tickets=FREE_ROUNDS_NUMBER_OF_TICKETS
        )
    yield {
        "campaign_id": str(uuid4()),
        "bonus_id": bonus_object["bonusObjectId"],
    }

