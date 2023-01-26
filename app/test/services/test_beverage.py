from app.test.utils.functions import get_random_string, get_random_price


def test_create_beverage_service(create_beverage):
    beverage = create_beverage.json
    assert create_beverage.status.startswith('200')
    assert beverage['_id']
    assert beverage['name']
    assert beverage['price']


def test_update_beverage_service(client, create_beverage, beverage_uri):
    current_beverage = create_beverage.json
    update_data = {**current_beverage, 'name': get_random_string(), 'price': get_random_price(1, 5)}
    response = client.put(beverage_uri, json=update_data)
    assert response.status.startswith('200'), f"status code is not 200, got {response.status}"
    updated_beverage = response.json
    for param, value in update_data.items():
        assert updated_beverage[param] == value, f"{param} does not match expected value"


def test_get_beverage_by_id_service(client, create_beverage, beverage_uri):
    current_beverage = create_beverage.json
    response = client.get(f'{beverage_uri}id/{current_beverage["_id"]}')
    assert response.status.startswith('200'), f"status code is not 200, got {response.status}"
    returned_beverage = response.json
    for param, value in current_beverage.items():
        assert returned_beverage[param] == value, f"{param} does not match expected value"


def test_get_beverages_service(client, create_beverages, beverage_uri):
    response = client.get(beverage_uri)
    assert response.status.startswith('200'), f"Unexpected status code: {response.status}"
    returned_beverages = {beverage['_id']: beverage for beverage in response.json}
    for beverage in create_beverages:
        assert beverage['_id'] in returned_beverages, f"{beverage['_id']} not found in returned beverages"
