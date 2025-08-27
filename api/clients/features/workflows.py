from typing import Optional
from requests import Session
from models import Operator
from logger import log
from models import Player
from .actions import OperatorActionsApi


class OperatorWorkflowsApi:
    def __init__(self, session: Optional[Session] = None, operator: Optional[Operator] = None):
        self.session = session
        self.operator = operator
        self.actions = OperatorActionsApi(session=session, operator=operator)

    def kyc_investigate(self, player: Player):
        log.debug(f"Starting Kyc investigation workflow for player {player}")
        self.actions.review_uploaded_document(player_id=player.player_id)
        self.actions.update_player_account_details(player_id=player.player_id, ssn=player.ssn)
        self.actions.manual_risk_kyc_review(player_id=player.player_id, ssn=player.ssn)
        log.info(f"Kyc investigation workflow completed successfully for player {player}")

    def approve_bank_account(self, player: Player, payment_method_id: Optional[str] = None):
        log.debug(f"Starting bank account approval workflow for player {player}")
        self.actions.review_uploaded_document(player_id=player.player_id,
                                              document_type="Financial",
                                              document_sub_type="Financial Institution Bank Statement",
                                              paymentMethodId=payment_method_id, plaiData=True)
        self.actions.giact_risk_review()
        self.actions.verify_bank_account(player_id=player.player_id)
        log.info(f"Bank account approval workflow completed successfully for player {player}")

    def approve_claim(self):
        log.debug("Starting claim approval workflow")
        self.actions.claim_review()
        self.actions.approve_latest_claim()
        log.info("Claim approval workflow completed successfully")

