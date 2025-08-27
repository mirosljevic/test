import re
from abc import ABC, abstractmethod
from utils.soup import fetch
from logger import log

TOKEN_REGEX = r'token=([a-f0-9\-]+)'
REQUEST_ID_REGEX = r'requestId=(\d+)'


class BaseEmailClient(ABC):
    def __init__(self, username):
        self.username = username
        self.email = None

    @abstractmethod
    def wait_for_email_with_subject(self, subject: str) -> str:
        """
        Waits for an email with the specified subject.

        :param subject: The subject of the email to wait for.
        :param retry_attempts: Number of attempts to check for the email.
        :param timeout: Time in seconds to wait between attempts.
        :return: The email message if found.
        """
        pass

    def get_registration_auth_details(self):
        try:
            message_body = self.wait_for_email_with_subject(subject="Verify your email address")
            link = list(filter(lambda x:"requestId" in str(x), fetch(message_body).find_all("a")))[0]["href"]
            token_match = re.search(TOKEN_REGEX, message_body)
            request_id_match = re.search(REQUEST_ID_REGEX, message_body)

            token = token_match.group(1) if token_match else None
            request_id = request_id_match.group(1) if request_id_match else None
            log.debug(f"Extracted details from message body => Token: {token}, Request ID: {request_id}")
            return request_id, token, link
        except Exception:
            log.error("Failed to extract token and request id!")
            raise
