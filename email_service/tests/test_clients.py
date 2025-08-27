from email_service import MailHogClient, MailinatorClient, TempMailClient


class TestEmailClients:
    def test_mailhog_client_initialization(self):
        client = MailHogClient("test@example.com")
        assert client.user == "test@example.com"
        assert client.host == "http://localhost:8025"

    def test_mailinator_client_initialization(self):
        client = MailinatorClient("test@mailinator.com")
        assert client.user == "test@mailinator.com"
        assert client.inbox == "test"

    def test_tempmail_client_initialization(self):
        client = TempMailClient("test@temp-mail.org")
        assert client.user == "test@temp-mail.org"
        assert client.email_hash is not None

    def test_create_account_methods(self):
        mailhog = MailHogClient("test@example.com")
        result = mailhog.create_account()
        assert result["success"] is True
        assert result["email"] == "test@example.com"

        mailinator = MailinatorClient("test@mailinator.com")
        result = mailinator.create_account()
        assert result["success"] is True
        assert "@mailinator.com" in result["email"]

        tempmail = TempMailClient()
        result = tempmail.create_account()
        assert "success" in result

    def test_get_emails_returns_list(self):
        clients = [
            MailHogClient("test@example.com"),
            MailinatorClient("test@mailinator.com"),
            TempMailClient("test@temp-mail.org")
        ]
        
        for client in clients:
            emails = client.get_emails()
            assert isinstance(emails, list)

    def test_get_message_returns_dict(self):
        clients = [
            MailHogClient("test@example.com"),
            MailinatorClient("test@mailinator.com"),
            TempMailClient("test@temp-mail.org")
        ]
        
        for client in clients:
            message = client.get_message("dummy_id")
            assert isinstance(message, dict)
