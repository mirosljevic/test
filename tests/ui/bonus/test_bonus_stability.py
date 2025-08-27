from pytest import mark
from models import InstantGames


@mark.stability
def test_bonus_stability(player):
    player.ui.open()
    player.ui.authentication.login()

    details = player.ui.bonus.get_latest_bonus()
    assert details["status"] == "Offer"

    player.api.bonus.achieve_bonus_offer(campaign_id=player.mongo.get("campaign_id"),
                                         player_id=player.player.player_id, bonus_id=player.mongo.get("bonus_id"))

    player.ui.page.reload()
    details = player.ui.bonus.get_latest_bonus()
    assert details["status"] == "Achieved"

    player.ui.instants.play_game(game=InstantGames.lucky_forest, rounds=3, bonus=True)

    details = player.ui.bonus.get_latest_bonus()
    assert details["status"] == "Used"
