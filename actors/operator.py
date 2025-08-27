from functools import cached_property
from .base import BaseActor
from models import Operator
from api.clients.operator_client import OperatorApiClient


class OperatorActor(BaseActor):
    def __init__(self, operator: Operator, browser=None, session=None, **kwargs):
        super().__init__(**kwargs)
        self.operator = operator
        self.browser = browser
        self.session = session

    @property
    def api(self):
        return OperatorApiClient(operator=self.operator, session=self.session)

    def authenticate(self):
        self.session = self.api.authentication.login()
