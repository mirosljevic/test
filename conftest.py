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
    # Create test-results directory if it doesn't exist
    os.makedirs("test-results/videos", exist_ok=True)
    os.makedirs("test-results/screenshots", exist_ok=True)
    
    browser = playwright.chromium.launch(
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
