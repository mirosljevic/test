import pytest
from models import Operator, OperatorRole


class TestOperator:
    def test_basic_operator_creation(self):
        operator = Operator(username="test_user", password="secure_password", role=OperatorRole.RISK_ANALYST)
        assert operator.username == "test_user"
        assert operator.password == "secure_password"
        assert operator.role == OperatorRole.RISK_ANALYST


if __name__ == "__main__":
    pytest.main([__file__])
