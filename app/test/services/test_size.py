from app.test.utils.functions import get_random_string, get_random_price


def test_create_size_service(create_size):
    size = create_size.json
    assert create_size.status.startswith('200'), f"Status code is not 200, got {create_size.status}"
    assert size['_id'], "Missing _id field in response"
    assert size['name'], "Missing name field in response"


def test_update_size_service(client, create_size, size_uri):
    current_size = create_size.json
    update_data = {**current_size, 'name': get_random_string(), 'price': get_random_price(1, 5)}
    response = client.put(size_uri, json=update_data)
    assert response.status.startswith('200'), f"Status code is not 200, got {response.status}"
    updated_size = response.json
    for param, value in update_data.items():
        assert updated_size[param] == value, f"{param} does not match expected value: {value}"


def test_get_size_by_id_service(client, create_size, size_uri):
    current_size = create_size.json
    response = client.get(f'{size_uri}id/{current_size["_id"]}')
    assert response.status.startswith('200'), f"Status code is not 200, got {response.status}"
    returned_size = response.json
    for param, value in current_size.items():
        assert returned_size[param] == value, f"{param} does not match expected value: {value}"


def test_get_sizes_service(client, create_sizes, size_uri):
    response = client.get(size_uri)
    assert response.status.startswith('200'), f"Status code is not 200, got {response.status}"
    returned_sizes = {size['_id']: size for size in response.json}
    for size in create_sizes:
        assert size['_id'] in returned_sizes, f"{size['_id']} not found in returned sizes"
