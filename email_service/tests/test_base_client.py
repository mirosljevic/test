from email_service.base import BaseEmailClient


class MockEmailClient(BaseEmailClient):
    def __init__(self, user: str, mock_emails: list = None):
        super().__init__(user)
        self.mock_emails = mock_emails or []

    def create_account(self):
        return {"success": True, "email": self.user}

    def get_message(self, message_id):
        for email in self.mock_emails:
            if email.get("message_id") == message_id:
                return email
        return {}

    def get_emails(self):
        return self.mock_emails


class TestBaseEmailClient:
    def test_initialization(self):
        client = MockEmailClient("test@example.com")
        assert client.user == "test@example.com"

    def test_get_email_with_subject(self):
        mock_emails = [
            {"subject": "Welcome", "body": "Hello"},
            {"subject": "Password reset", "body": "Reset link"},
        ]
        client = MockEmailClient("test@example.com", mock_emails)
        
        email = client.get_email_with_subject("password")
        assert email is not None
        assert "Password reset" in email["subject"]

    def test_get_token(self):
        mock_emails = [
            {"subject": "Verification", "body": "Your token: abc123xyz"},
        ]
        client = MockEmailClient("test@example.com", mock_emails)
        
        token = client.get_token()
        assert token == "abc123xyz"

    def test_get_request_id(self):
        mock_emails = [
            {"subject": "Request", "body": "Request ID: REQ-456"},
        ]
        client = MockEmailClient("test@example.com", mock_emails)
        
        request_id = client.get_request_id()
        assert request_id == "REQ-456"

    def test_wait_for_email(self):
        mock_emails = [
            {"subject": "Registration", "body": "Welcome"},
        ]
        client = MockEmailClient("test@example.com", mock_emails)
        
        email = client.wait_for_email("registration", timeout=1)
        assert email is not None
        assert "Registration" in email["subject"]

    def test_get_registration_details(self):
        mock_emails = [
            {"subject": "Registration", "body": "Token: xyz789 Request ID: REQ-123"},
        ]
        client = MockEmailClient("test@example.com", mock_emails)
        
        details = client.get_registration_details("registration")
        assert details["token"] == "xyz789"
        assert details["request_id"] == "REQ-123"
        assert details["email"] is not None
