from time import sleep
from logger import log
from ..base import BaseEmailClient
from .endpoints import get_messages
from .config import RETRIES_COUNT, RETRY_DELAY, DOMAIN


class MailHogClient(BaseEmailClient):
    def __init__(self, username):
        super().__init__(username)

    def create_account(self) -> str:
        self.email = f"{self.username}@{DOMAIN}"
        return self.email

    def wait_for_email_with_subject(self, subject: str) -> str:
        log.debug(f"Waiting for email with subject: {subject}")
        for _ in range(RETRIES_COUNT):
            try:
                messages = get_messages(self.email).json()['items']
                for message in messages:
                    if subject in message["Content"]["Headers"]["Subject"]:
                        log.debug(f"Email found with subject: {subject}")
                        return message["Content"]["Body"]
                log.warning(f"No email found with subject: {subject}. Retrying...")
            except Exception as e:
                log.error(f"Error fetching emails: {e}")
            sleep(RETRY_DELAY)
        
        log.error(f"Email with subject '{subject}' not found after {RETRIES_COUNT} retries")
        raise TimeoutError(f"Email with subject '{subject}' not found after {RETRIES_COUNT} retries")
