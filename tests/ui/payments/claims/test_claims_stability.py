from pytest import mark


@mark.stability
def test_claims_stability(player, risk_manager):
    player.ui.open()
    player.ui.authentication.login()

    player.ui.claims.claim_latest_item()
    claim = player.ui.claims.get_latest_claim()
    assert claim["status"] == "In Progress"

    risk_manager.api.workflows.approve_claim()

