from pytest import fixture
from requests import Session
from unittest.mock import MagicMock
from playwright.sync_api import Browser
from mongo import MongoClient
from logger import log


# @fixture(scope="session")
# def browser():
#     browser = MagicMock(spec=Browser)
#     return browser


@fixture(scope="session")
def mongo():
    mongo = MongoClient()
    return mongo


@fixture(scope="session")
def session():
    return Session()

