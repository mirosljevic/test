from requests import Session
from typing import Optional
from time import sleep

from logger import log
from models import Player
from api.endpoints.document.document_web import upload_document, get_requests


class PlayerDocumentsApi:
    def __init__(self, session: Optional[Session] = None, player: Optional[Player] = None):
        self.session = session
        self.player = player

    def upload(self, document_path: str = "files/documents/sample.pdf", wait_for_request=False) -> None:
        if wait_for_request:
            log.debug("Waiting for requests")
            self.wait_for_requests()
        log.debug(f"Uploading document: {document_path}")
        upload_document(
            session=self.session,
            document_type="LEGAL_AFFIDAVIT",
            file_location=document_path
        )
        return True

    def wait_for_requests(self, retries=20, timeout=1):
        retry = 1
        while retry <= retries:
            requests = get_requests(self.session).json()
            if len(requests["pageItems"]) > 0:
                log.info(f"Requests found: {requests['pageItems']}")
                return requests
            log.warning(f"No requests found. Retrying in {timeout} seconds")
            sleep(timeout)
            retry += 1
        log.error("No requests found")