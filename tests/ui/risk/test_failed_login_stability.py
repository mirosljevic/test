from pytest import mark

RETRY_ATTEMPTS = 5


@mark.stability
@mark.risk
def test_failed_login_stability():
    pass
