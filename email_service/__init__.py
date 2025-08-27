from .temp_mail.client import TempMailClient
from .mailhog.client import MailHogClient
from .mailinator.client import MailinatorClient
from environment import settings
from logger import log

if settings.email_provider == "mailhog":
    EmailClient = MailHogClient
elif settings.email_provider == "tempmail":
    EmailClient = TempMailClient
elif settings.email_provider == "mailinator":
    EmailClient = MailinatorClient
else:
    log.error(f"Unsupported email provider: {settings.email_provider}. Supported providers are 'mailhog', 'mailinator'. and 'tempmail'.")
    raise ValueError

__all__ = ["EmailClient", "TempMailClient", "MailHogClient"]