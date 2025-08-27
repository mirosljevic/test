"""
Global pytest configuration for the test automation framework.
"""
import pytest
import os
from playwright.sync_api import Playwright, Browser
from requests import Session
from mongo import MongoClient
from logger import log


@pytest.fixture(scope="session")
def playwright():
    """Playwright instance fixture."""
    with Playwright() as playwright_instance:
        yield playwright_instance


@pytest.fixture(scope="session")
def browser(playwright):
    """Browser instance fixture."""
    import os
    
    # Create test-results directory if it doesn't exist
    os.makedirs("test-results/videos", exist_ok=True)
    os.makedirs("test-results/screenshots", exist_ok=True)
    
    # Get browser type from environment variable
    device = os.getenv('DEVICE', 'chrome').lower()
    
    # Map device names to browser types
    browser_map = {
        'chrome': 'chromium',
        'chromium': 'chromium',
        'firefox': 'firefox',
        'safari': 'webkit',
        'webkit': 'webkit',
        'desktop': 'chromium',
        'mobile': 'chromium',
        'tablet': 'chromium'
    }
    
    browser_type = browser_map.get(device, 'chromium')
    log.info(f"Using browser: {browser_type} (requested: {device})")
    
    # Get the browser launcher
    if browser_type == 'firefox':
        browser_launcher = playwright.firefox
    elif browser_type == 'webkit':
        browser_launcher = playwright.webkit
    else:
        browser_launcher = playwright.chromium
    
    browser = browser_launcher.launch(
        headless=True,
        args=[
            "--no-sandbox",
            "--disable-dev-shm-usage",
            "--disable-gpu",
            "--disable-web-security",
            "--disable-features=VizDisplayCompositor"
        ]
    )
    yield browser
    browser.close()


@pytest.fixture(scope="session")
def session():
    """HTTP session fixture."""
    return Session()


@pytest.fixture(scope="session")
def mongo():
    """MongoDB client fixture."""
    mongo = MongoClient()
    return mongo
