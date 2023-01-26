import pytest

from ..utils.functions import get_random_price, get_random_string


@pytest.fixture
def beverage_mock() -> dict:
    return {
        'name': get_random_string(),
        'price': get_random_price(10, 20)
    }


@pytest.fixture
def beverage_uri():
    return '/beverage/'







@pytest.fixture
def create_beverage(client, beverage_uri, beverage_mock) -> dict:
    response = client.post(beverage_uri, json=beverage_mock)
    return response


@pytest.fixture
def create_beverages(client, beverage_uri, beverage_mock) -> list:
    beverages = []
    for _ in range(10):
        new_beverage = client.post(beverage_uri, json=beverage_mock)
        beverages.append(new_beverage.json)
    return beverages
