# Email Service Framework 📧

Advanced email testing framework with multi-provider support, temporary email services, and comprehensive email validation capabilities.

## Overview

The email service framework provides robust email automation testing with support for multiple email providers, temporary email services, and advanced email content validation for comprehensive testing workflows.

## Key Features

- **Multi-Provider Support**: Mailinator, MailHog, TempMail integration
- **Email Verification**: Link extraction and validation
- **Content Validation**: HTML/text parsing and validation
- **Real-time Monitoring**: Email status monitoring and reporting
- **Attachment Support**: File attachment handling
- **Template Testing**: Email template validation

## Architecture

```
email_service/
├── __init__.py              # Package initialization
├── base.py                  # Base email service class
├── mailinator_client.py     # Mailinator API client
├── status_overview.py       # Email status monitoring
├── README.md               # This documentation
├── mailhog/                # MailHog integration
│   ├── __init__.py
│   └── client.py
├── temp_mail/              # Temporary email services
│   ├── __init__.py
│   └── providers.py
├── samples/                # Usage examples
│   └── email_examples.py
└── tests/                  # Email service tests
    └── test_email_clients.py
```

## Core Components

### Base Email Service
```python
from email_service.base import BaseEmailService

class BaseEmailService:
    def __init__(self, provider: str = "mailinator"):
        self.provider = provider
        self.client = self._create_client()
    
    def get_emails(self, email_address: str) -> List[Dict]:
        """Get all emails for address."""
        return self.client.get_emails(email_address)
    
    def get_latest_email(self, email_address: str) -> Dict:
        """Get most recent email."""
        emails = self.get_emails(email_address)
        return emails[0] if emails else None
    
    def extract_verification_link(self, email_content: str) -> str:
        """Extract verification link from email content."""
        # Implementation for link extraction
        pass
    
    def wait_for_email(self, email_address: str, subject_contains: str = None, 
                      timeout: int = 60) -> Dict:
        """Wait for email with specific criteria."""
        # Implementation for waiting
        pass
```

### Mailinator Client
```python
from email_service.mailinator_client import MailinatorClient

class MailinatorClient:
    def __init__(self, api_token: str):
        self.api_token = api_token
        self.base_url = "https://api.mailinator.com/v4"
        self.headers = {
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        }
    
    def get_inbox(self, inbox_name: str) -> Dict:
        """Get inbox contents."""
        url = f"{self.base_url}/inboxes/{inbox_name}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_email(self, inbox_name: str, email_id: str) -> Dict:
        """Get specific email by ID."""
        url = f"{self.base_url}/inboxes/{inbox_name}/messages/{email_id}"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def get_email_content(self, inbox_name: str, email_id: str) -> str:
        """Get email HTML content."""
        url = f"{self.base_url}/inboxes/{inbox_name}/messages/{email_id}/body"
        response = requests.get(url, headers=self.headers)
        return response.text
    
    def delete_inbox(self, inbox_name: str) -> bool:
        """Delete entire inbox."""
        url = f"{self.base_url}/inboxes/{inbox_name}"
        response = requests.delete(url, headers=self.headers)
        return response.status_code == 200
```

## Email Verification

### Link Extraction
```python
import re
from bs4 import BeautifulSoup
from urllib.parse import urlparse, parse_qs

class EmailVerification:
    @staticmethod
    def extract_verification_links(email_content: str) -> List[str]:
        """Extract all verification links from email."""
        soup = BeautifulSoup(email_content, 'html.parser')
        links = []
        
        # Find all links
        for link in soup.find_all('a', href=True):
            href = link['href']
            if 'verify' in href.lower() or 'confirm' in href.lower():
                links.append(href)
        
        # Also check for plain text links
        url_pattern = r'https?://[^\s<>"]+(?:verify|confirm)[^\s<>"]*'
        text_links = re.findall(url_pattern, email_content, re.IGNORECASE)
        links.extend(text_links)
        
        return links
    
    @staticmethod
    def extract_verification_tokens(email_content: str) -> List[str]:
        """Extract verification tokens from email."""
        # Pattern for common token formats
        token_patterns = [
            r'token=([a-zA-Z0-9]+)',
            r'verification[_-]?token["\':=\s]+([a-zA-Z0-9-_]+)',
            r'confirm[_-]?code["\':=\s]+([a-zA-Z0-9-_]+)'
        ]
        
        tokens = []
        for pattern in token_patterns:
            matches = re.findall(pattern, email_content, re.IGNORECASE)
            tokens.extend(matches)
        
        return tokens
    
    @staticmethod
    def extract_reset_passwords_links(email_content: str) -> List[str]:
        """Extract password reset links."""
        soup = BeautifulSoup(email_content, 'html.parser')
        links = []
        
        for link in soup.find_all('a', href=True):
            href = link['href']
            if any(keyword in href.lower() for keyword in ['reset', 'password', 'forgot']):
                links.append(href)
        
        return links
```

### Email Content Validation
```python
class EmailContentValidator:
    def __init__(self, email_content: str):
        self.content = email_content
        self.soup = BeautifulSoup(email_content, 'html.parser')
    
    def has_subject(self, expected_subject: str) -> bool:
        """Check if email has expected subject."""
        # Implementation depends on email structure
        pass
    
    def contains_text(self, text: str) -> bool:
        """Check if email contains specific text."""
        return text.lower() in self.content.lower()
    
    def has_verification_link(self) -> bool:
        """Check if email contains verification link."""
        links = EmailVerification.extract_verification_links(self.content)
        return len(links) > 0
    
    def has_unsubscribe_link(self) -> bool:
        """Check if email contains unsubscribe link."""
        for link in self.soup.find_all('a', href=True):
            if 'unsubscribe' in link['href'].lower():
                return True
        return False
    
    def validate_branding(self, brand_elements: List[str]) -> bool:
        """Validate brand elements in email."""
        for element in brand_elements:
            if not self.contains_text(element):
                return False
        return True
    
    def get_all_links(self) -> List[str]:
        """Get all links from email."""
        links = []
        for link in self.soup.find_all('a', href=True):
            links.append(link['href'])
        return links
    
    def get_images(self) -> List[str]:
        """Get all image sources from email."""
        images = []
        for img in self.soup.find_all('img', src=True):
            images.append(img['src'])
        return images
```

## Email Providers

### MailHog Integration
```python
from email_service.mailhog.client import MailHogClient

class MailHogClient:
    def __init__(self, base_url: str = "http://localhost:8025"):
        self.base_url = base_url
        self.api_url = f"{base_url}/api/v2"
    
    def get_messages(self, limit: int = 50) -> List[Dict]:
        """Get all messages from MailHog."""
        url = f"{self.api_url}/messages?limit={limit}"
        response = requests.get(url)
        return response.json().get('items', [])
    
    def search_messages(self, query: str) -> List[Dict]:
        """Search messages by query."""
        url = f"{self.api_url}/search"
        params = {'kind': 'containing', 'query': query}
        response = requests.get(url, params=params)
        return response.json().get('items', [])
    
    def get_message_by_id(self, message_id: str) -> Dict:
        """Get specific message by ID."""
        url = f"{self.api_url}/messages/{message_id}"
        response = requests.get(url)
        return response.json()
    
    def delete_all_messages(self) -> bool:
        """Delete all messages from MailHog."""
        url = f"{self.api_url}/messages"
        response = requests.delete(url)
        return response.status_code == 200
```

### Temporary Email Services
```python
from email_service.temp_mail.providers import TempMailProvider

class TempMailProvider:
    def generate_email(self) -> str:
        """Generate temporary email address."""
        pass
    
    def get_emails(self, email_address: str) -> List[Dict]:
        """Get emails for temporary address."""
        pass
    
    def cleanup_email(self, email_address: str) -> bool:
        """Clean up temporary email address."""
        pass

class TenMinuteMailProvider(TempMailProvider):
    def __init__(self):
        self.base_url = "https://10minutemail.com/api"
    
    def generate_email(self) -> str:
        """Generate 10-minute email address."""
        response = requests.get(f"{self.base_url}/generate")
        return response.json()['email']
    
    def get_emails(self, email_address: str) -> List[Dict]:
        """Get emails for 10-minute address."""
        response = requests.get(f"{self.base_url}/messages/{email_address}")
        return response.json().get('messages', [])
```

## Usage Examples

### Registration Email Verification
```python
from email_service import EmailService

def test_player_registration_email(player_actor, email_service):
    """Test player registration sends verification email."""
    # Generate temporary email
    temp_email = email_service.generate_temporary_email()
    
    # Register player with temp email
    player_actor.player.email = temp_email
    result = player_actor.register()
    assert result.success
    
    # Wait for verification email
    email = email_service.wait_for_email(
        email_address=temp_email,
        subject_contains="Verify your account",
        timeout=60
    )
    assert email is not None
    
    # Validate email content
    validator = EmailContentValidator(email['content'])
    assert validator.has_verification_link()
    assert validator.contains_text("Welcome")
    assert validator.has_unsubscribe_link()
    
    # Extract and use verification link
    verification_links = EmailVerification.extract_verification_links(email['content'])
    assert len(verification_links) > 0
    
    # Complete verification
    player_actor.page.goto(verification_links[0])
    assert player_actor.ui.account.is_verified()
```

### Password Reset Flow
```python
def test_password_reset_email(player_actor, email_service):
    """Test password reset email flow."""
    # Setup: Register and verify player
    player_actor.register()
    player_actor.verify_email()
    
    # Request password reset
    player_actor.ui.forgot_password.request_reset(player_actor.player.email)
    
    # Wait for reset email
    reset_email = email_service.wait_for_email(
        email_address=player_actor.player.email,
        subject_contains="Password Reset",
        timeout=60
    )
    assert reset_email is not None
    
    # Extract reset link
    reset_links = EmailVerification.extract_reset_passwords_links(reset_email['content'])
    assert len(reset_links) > 0
    
    # Use reset link
    new_password = "NewPassword123!"
    player_actor.page.goto(reset_links[0])
    player_actor.ui.password_reset.set_new_password(new_password)
    
    # Verify can login with new password
    player_actor.player.password = new_password
    login_result = player_actor.login()
    assert login_result.success
```

### Email Template Testing
```python
def test_welcome_email_template(email_service):
    """Test welcome email template content."""
    # Get latest welcome email
    email = email_service.get_latest_email("test@mailinator.com")
    validator = EmailContentValidator(email['content'])
    
    # Brand validation
    brand_elements = ["Your Casino", "Welcome", "Get Started"]
    assert validator.validate_branding(brand_elements)
    
    # Link validation
    links = validator.get_all_links()
    assert any("dashboard" in link for link in links)
    assert any("support" in link for link in links)
    
    # Image validation
    images = validator.get_images()
    assert len(images) > 0
    assert any("logo" in img for img in images)
    
    # Required elements
    assert validator.has_unsubscribe_link()
    assert validator.contains_text("Terms and Conditions")
```

## Status Monitoring

### Email Status Overview
```python
from email_service.status_overview import EmailStatusMonitor

class EmailStatusMonitor:
    def __init__(self, providers: List[str] = None):
        self.providers = providers or ['mailinator', 'mailhog']
        self.status_data = {}
    
    def check_provider_status(self, provider: str) -> Dict:
        """Check status of email provider."""
        if provider == 'mailinator':
            return self._check_mailinator_status()
        elif provider == 'mailhog':
            return self._check_mailhog_status()
    
    def generate_status_report(self) -> Dict:
        """Generate comprehensive status report."""
        report = {
            'timestamp': datetime.now().isoformat(),
            'providers': {},
            'summary': {}
        }
        
        for provider in self.providers:
            status = self.check_provider_status(provider)
            report['providers'][provider] = status
        
        # Generate summary
        total_providers = len(self.providers)
        healthy_providers = sum(1 for p in report['providers'].values() 
                              if p.get('status') == 'healthy')
        
        report['summary'] = {
            'total_providers': total_providers,
            'healthy_providers': healthy_providers,
            'overall_status': 'healthy' if healthy_providers == total_providers else 'degraded'
        }
        
        return report
```

## Configuration

### Provider Settings
```python
# settings/email_service.py
EMAIL_SETTINGS = {
    'mailinator': {
        'api_token': os.getenv('MAILINATOR_API_TOKEN'),
        'base_url': 'https://api.mailinator.com/v4'
    },
    'mailhog': {
        'base_url': os.getenv('MAILHOG_URL', 'http://localhost:8025')
    },
    'temp_mail': {
        'provider': '10minutemail',
        'cleanup_after_test': True
    }
}
```

## Best Practices

1. **Provider Reliability**: Use multiple providers for redundancy
2. **Email Cleanup**: Clean up temporary emails after tests
3. **Content Validation**: Validate both HTML and text content
4. **Link Security**: Validate all links in emails
5. **Template Testing**: Test email templates across different clients
6. **Performance**: Monitor email delivery times
7. **Security**: Validate unsubscribe and privacy links
8. **Accessibility**: Test email accessibility features

## Integration

The email service integrates with:
- **Actors**: Email verification workflows for test personas
- **UI Framework**: Email-based user flows
- **API Framework**: Email API endpoint testing
- **Data Factory**: Test email generation
- **Environment**: Multi-environment email configuration
- **Logger**: Email operation logging and monitoring
