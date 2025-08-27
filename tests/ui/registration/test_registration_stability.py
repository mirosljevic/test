from pytest import mark


@mark.stability
def test_registration_stability(player):
    player.ui.open()

    player.ui.registration.go_to_registration()
    player.player = player.ui.registration.submit_registration()

    player.ui.authentication.login()
    profile = player.ui.account.get_account_profile()

    assert profile["name"] == player.player.full_name
    assert profile["email"] == player.player.email
    assert profile["ssn"] == player.player.ssn_last_four
    assert profile["mobile"] == player.player.phone
    assert profile["address"]["address"] == player.player.address
    assert profile["address"]["city"] == player.player.city
    assert profile["address"]["state"] == player.player.state
    assert profile["address"]["zip_code"] == player.player.zip_code
    assert profile["dob"] == player.player.date_of_birth

