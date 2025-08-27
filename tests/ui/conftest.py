from pytest import fixture
from requests import Session
from mongo import MongoClient
from logger import log


# Browser fixture is now defined in the global conftest.py

@fixture(scope="session")
def mongo():
    mongo = MongoClient()
    return mongo


@fixture(scope="session")
def session():
    return Session()

