from time import sleep
from logger import log
from ..base import BaseEmailClient
from .config import RETRIES_COUNT, RETRY_DELAY
from .endpoints import get_domains, create_account, get_token, get_messages, get_message


class TempMailClient(BaseEmailClient):
    def __init__(self, username):
        super().__init__(username)
        self.password = "temporary_password"
        self.token = None

    @staticmethod
    def get_available_domain() -> str:
        log.debug("Fetching available domains from Temp Mail API")
        response = get_domains()

        domains = response.json().get("hydra:member", [])

        if domains:
            return domains[0].get("domain")
        else:
            log.error("No available domains found in Temp Mail API response")
            return ""

    def create_account(self) -> dict:
        log.debug("Creating new temporary email account")
        try:
            domain = self.get_available_domain()
            if not domain:
                log.exception("No available domains found")
            email = f"{self.username}@{domain}"
            create_account(email, self.password)
            self.email = email
            self.token = get_token(email, self.password).json().get("token")
            return email
        except Exception as e:
            log.error(f"Error creating temporary email: {e}")
            raise

    def wait_for_email_with_subject(self, subject: str) -> str:
        log.debug(f"Waiting for email with subject: {subject}")
        for attempt in range(RETRIES_COUNT):
            try:
                messages = get_messages(self.token).json().get("hydra:member", [])
                for message in messages:
                    if message.get("subject") == subject:
                        log.debug(f"Email found with subject: {subject}")
                        return get_message(self.token, message.get("id")).json()["html"][0]
                log.warning(f"No email found with subject: {subject}. Retrying...")
            except Exception as e:
                log.error(f"Error fetching emails: {e}")
            sleep(RETRY_DELAY)
        log.error(f"Email with subject '{subject}' not found after {RETRIES_COUNT} attempts")
        raise TimeoutError(f"Email with subject '{subject}' not found after {RETRIES_COUNT} attempts")
