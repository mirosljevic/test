from requests import Session
from typing import Optional
from contextlib import contextmanager

from models import Operator
from mongo import OperatorMongoClient
from logger import log

from .base import BaseAPIClient
from .features.authentication import OperatorAuthenticationApi
from .features.account import OperatorAccountApi
# from .features.payments import OperatorPaymentsApi
# from .features.documents import OperatorDocumentsApi
from .features.bonus import OperatorBonusApi
from .features.workflows import OperatorWorkflowsApi


class OperatorApiClient(BaseAPIClient):
    def __init__(self, operator: Optional[Operator] = None, session: Optional[Session] = None, mongo=None):
        self.operator = operator
        self.session = session
        self.mongo = mongo or OperatorMongoClient(operator=operator)

    @property
    def authentication(self) -> OperatorAuthenticationApi:
        return OperatorAuthenticationApi(session=self.session, operator=self.operator)
    
    @property
    def account(self) -> OperatorAccountApi:
        return OperatorAccountApi(session=self.session, operator=self.operator)

    @property
    def bonus(self) -> OperatorBonusApi:
        return OperatorBonusApi(session=self.session, operator=self.operator)

    @property
    def workflows(self):
        return OperatorWorkflowsApi(session=self.session, operator=self.operator)

    def authenticate(self):
        self.session = self.authentication.login()
