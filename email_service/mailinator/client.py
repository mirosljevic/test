from time import sleep
from requests import Session
from logger import log
from .config import MAILINATOR_DOMAIN, RETRIES_COUNT, RETRY_DELAY
from .endpoints import get_messages, get_message
from ..base import BaseEmailClient


class MailinatorClient(BaseEmailClient):
    def __init__(self, username):
        super().__init__(username)
        self.session = Session()

    def create_account(self) -> str:
        self.email = f"{self.username}@{MAILINATOR_DOMAIN}"
        return self.email

    def wait_for_email_with_subject(self, subject: str) -> str:
        log.debug(f"Waiting for email with subject: {subject}")
        for _ in range(RETRIES_COUNT):
            try:
                response = get_messages(self.session, self.username).json()
                messages = response.get('msgs', [])
                for message in messages:
                    if subject in message["subject"]:
                        log.debug(f"Email found with subject: {subject}")
                        return get_message(self.session, self.username, message["id"]).json()["parts"][0]["body"]
                log.warning(f"No email found with subject: {subject}. Retrying...")
            except Exception as e:
                log.error(f"Error fetching emails: {e}")
            sleep(RETRY_DELAY)

        log.error(f"Email with subject '{subject}' not found after {RETRIES_COUNT} retries")
        raise TimeoutError(f"Email with subject '{subject}' not found after {RETRIES_COUNT} retries")