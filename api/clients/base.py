"""
Base API Client

Shared functionality for all API clients including initialization,
base URL management, token handling, and API executor integration.
"""

from logger import log


class BaseAPIClient:
    """
    Base class for all API clients providing common functionality.

    This class handles:
    - Base URL configuration
    - Authentication token management
    - API executor initialization
    - Common logging patterns
    """

    def __init__(self, base_url=None, token=None, timeout=30):
        """
        Initialize the base API client.

        Args:
            base_url (str, optional): Base URL for API endpoints
            token (str, optional): Authentication token
            timeout (int, optional): Request timeout in seconds
        """
        self.base_url = base_url or self._get_default_base_url()
        self.token = token
        self.timeout = timeout

        # Store default headers for future requests
        self.default_headers = self._get_default_headers()

        # Note: ApiExecutor will be instantiated per request in actual
        # implementation
        self.executor = None  # Placeholder for now

        log.debug(
            f"Initialized {self.__class__.__name__} with base_url: {self.base_url}"
        )

    def _get_default_base_url(self):
        """
        Get the default base URL for this client type.
        Override in subclasses to provide client-specific defaults.

        Returns:
            str: Default base URL
        """
        return "https://api.example.com"

    def _get_default_headers(self):
        """
        Get default headers for API requests.

        Returns:
            dict: Default headers including authentication if token is provided
        """
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"}

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
            log.debug("Added authentication token to default headers")

        return headers

    def set_token(self, token):
        """
        Update the authentication token for this client.

        Args:
            token (str): New authentication token
        """
        self.token = token
        self.default_headers["Authorization"] = f"Bearer {token}"
        log.debug("Updated authentication token")

    def clear_token(self):
        """Remove authentication token from this client."""
        self.token = None
        if "Authorization" in self.default_headers:
            del self.default_headers["Authorization"]
        log.debug("Cleared authentication token")

    def update_base_url(self, base_url):
        """
        Update the base URL for this client.

        Args:
            base_url (str): New base URL
        """
        self.base_url = base_url
        log.debug(f"Updated base URL to: {base_url}")

    def get_client_info(self):
        """
        Get information about this client instance.

        Returns:
            dict: Client configuration information
        """
        return {
            "client_type": self.__class__.__name__,
            "base_url": self.base_url,
            "has_token": bool(self.token),
            "timeout": self.timeout,
        }
