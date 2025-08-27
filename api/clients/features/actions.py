import json
from typing import Optional
from requests import Session
from models import Operator
from logger import log
from .tasks import OperatorTasksApi
from api.endpoints.customer.customer_cc import request_verifications


class OperatorActionsApi:
    def __init__(self, session: Optional[Session] = None, operator: Optional[Operator] = None):
        self.session = session
        self.operator = operator
        self.tasks = OperatorTasksApi(session, operator)

    def review_uploaded_document(self, player_id, document_type="LEGAL_AFFIDAVIT",
                                 document_sub_type="AFFIDAVIT_SSN9_VERIFICATION", issue_date="2024-09-09", **kwargs):
        payload = {
            "playerId": player_id,
            "type": document_type,
            "subType": document_sub_type,
            "status": "APPROVED",
            "subStatus": "APPROVED",
            "documentEditRequired": False,
            "issueDate": issue_date, **kwargs}
        self.tasks.claim_and_complete_task(
            task_name="Review Uploaded Document",
            player_id=player_id,
            payload=payload)
        log.info("Document reviewed successfully")
        return True

    def update_player_account_details(self, player_id, ssn):
        data = json.dumps({"ssn": ssn.replace("-", "")})
        payload = {
            "playerAccountUpdateResult": "updateKycData",
            "changedPlayerData": data}
        self.tasks.claim_and_complete_task(
            task_name="Update Player Account Details",
            player_id=player_id,
            payload=payload)
        log.debug("Player account details updated successfully")
        return True

    def manual_risk_kyc_review(self, player_id, ssn):
        request_verifications(session=self.session, player_id=player_id, ssn=ssn)
        payload = {
            "manualFailureReviewResult": "approve",
            "pendingVerifications": ["ssn"]}
        self.tasks.claim_and_complete_task(
            task_name="Manual Risk Review of KYC Investigation",
            player_id=player_id,
            payload=payload)
        log.debug("Manual Risk KYC Review completed successfully")
        return True

    def claim_review(self):
        self.tasks.claim_and_complete_task(
            task_name="Claim Review",
            payload={
                "contactPlayerByCsc": False,
                "contactPlayerByRisk": False,
                "documentRequest": False,
                "relateCase": False,
                "relateCaseInfoList": [],
                "requestDocumentInfoList": [],
                "riskReviewResult": "approve"
            })
        log.debug("Claim reviewed successfully")
        return True

