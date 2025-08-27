from argparse import ArgumentParser
from uuid import uuid4
from contextlib import contextmanager
from data_factory import create_player, create_credit_card
from actors import PlayerActor, OperatorActor
from mongo import PlayerMongoClient, MongoClient
from models import InstantGames
from logger import log


@contextmanager
def new_player():
    player_data = create_player()
    player_actor = PlayerActor(player=player_data)
    player_data = player_actor.api.registration.register()
    player_mongo = PlayerMongoClient(player=player_data)
    player_mongo.insert()
    player_actor.mongo.update(type="unverified_player")
    yield player_actor


@contextmanager
def new_player_session():
    with new_player() as player:
        player.mongo.lock()
        player.authenticate()
        yield player
        player.mongo.set_available()


@contextmanager
def risk_analyst_session():
    risk_analyst_mongo = MongoClient().get_available_operator(role="Risk Analyst")
    risk_analyst_mongo.lock()
    risk_analyst_actor = OperatorActor(operator=risk_analyst_mongo.operator)
    risk_analyst_actor.authenticate()
    yield risk_analyst_actor
    risk_analyst_mongo.set_available()


@contextmanager
def marketing_analyst_session():
    marketing_analyst_mongo = MongoClient().get_available_operator(role="Marketing Analyst")
    marketing_analyst_mongo.lock()
    marketing_analyst_actor = OperatorActor(operator=marketing_analyst_mongo.operator)
    marketing_analyst_actor.authenticate()
    yield marketing_analyst_actor
    marketing_analyst_mongo.set_available()


@contextmanager
def verified_player_session():
    with risk_analyst_session() as risk_analyst:
        with new_player_session() as player:
            player.api.documents.upload(wait_for_request=True)
            risk_analyst.api.workflows.kyc_investigate(player=player.player)
            player.mongo.update(type="verified_player")
            yield player


@contextmanager
def bonus_player_session():
    with marketing_analyst_session() as marketing_analyst:
        with verified_player_session() as player:
            bonus_object = marketing_analyst.api.bonus.get_bonus_object(name="Free Rounds AUTOMATED")
            if not bonus_object:
                bonus_object = marketing_analyst.api.bonus.create_free_rounds_object(
                    games=["LF"],
                    cost_per_ticket=1,
                    object_name="Free Rounds AUTOMATED",
                    number_of_rounds=3,
                    number_of_tickets=1
                )
            campaign_id = str(uuid4())
            bonus_id = bonus_object["bonusObjectId"]
            player.api.bonus.create_bonus_offer(campaign_id=campaign_id, bonus_id=bonus_id)
            player.mongo.update(type="bonus_player", campaign_id=campaign_id, bonus_id=bonus_id)
            yield player


@contextmanager
def depositor_session():
    with verified_player_session() as player:
        card = create_credit_card(card_type="visa")
        player.api.payments.add_credit_card(credit_card=card)
        player.api.payments.make_deposit(credit_card=card, amount=1000)
        player.mongo.update(type="depositor")
        yield player


@contextmanager
def winner_session():
    with depositor_session() as player:
        player.api.instants.play_and_win(game=InstantGames.lucky_forest, prize_amount=30)
        player.mongo.update(type="winner")
        yield player


@contextmanager
def high_value_winner_session():
    with depositor_session() as player:
        player.api.instants.play_game(game=InstantGames.prize_testing_game, highest_bet=True)
        player.mongo.update(type="high_value_winner")
        yield player


def parse_args():
    parser = ArgumentParser(description="API Sessions Management")
    parser.add_argument("--players", type=int, default=1, help="Number of players")
    parser.add_argument("--type", type=str, default="unverified_player", help="Player type")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    success_count = 0
    failure_count = 0

    if args.type not in ["unverified_player", "bonus_player", "verified_player", "depositor", "winner", "high_value_winner"]:
        raise ValueError(f"Unsupported player type: {args.type}")

    for _ in range(args.players):
        try:
            if args.type == "unverified_player":
                player = new_player()
            elif args.type == "bonus_player":
                player = bonus_player_session()
            elif args.type == "verified_player":
                player = verified_player_session()
            elif args.type == "depositor":
                player = depositor_session()
            elif args.type == "winner":
                player = winner_session()
            elif args.type == "high_value_winner":
                player = high_value_winner_session()

            with player as player:
                log.info(f"Player created: {player.player}, Type: {args.type}")

            success_count += 1
        except Exception as e:
            log.error(f"Error creating player: {e}")
            failure_count += 1

    log.info(f"Total players created: {success_count}, Failed: {failure_count}")
