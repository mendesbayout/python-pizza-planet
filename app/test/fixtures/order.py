import pytest
from faker import Faker

from app.repositories.models import Ingredient, Beverage


def client_data_mock() -> dict:
    fake = Faker()
    return {
        'client_address': fake.address(),
        'client_dni': fake.random_number(digits=8),
        'client_name': fake.name(),
        'client_phone': fake.phone_number()
    }


@pytest.fixture
def order_uri():
    return '/order/'


@pytest.fixture
def client_data():
    return client_data_mock()


@pytest.fixture
def clients_data():
    return [client_data_mock() for _ in range(3)]


@pytest.fixture
def order(create_beverages, create_ingredients, create_size, client_data) -> dict:
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    size_id = create_size.json['_id']
    order_data = {
        **client_data,
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }
    return order_data


@pytest.fixture
def create_order(create_beverages, create_ingredients, create_size, client_data):
    ingredients = [ingredient.get('_id') for ingredient in create_ingredients]
    beverages = [beverage.get('_id') for beverage in create_beverages]
    size_id = create_size.json['_id']
    order_data = {
        **client_data,
        'ingredients': ingredients,
        'beverages': beverages,
        'size_id': size_id
    }
    return order_data


@pytest.fixture
def get_order_by_id_service():
    fake = Faker()
    order = {
        '_id': fake.uuid4(),
        'client_name': fake.name(),
        'client_dni': fake.random_number(digits=8),
        'client_address': fake.address(),
        'client_phone': fake.phone_number(),
        'date': fake.date_time_this_decade(),
        'total_price': fake.random_number(),
        'size': {'_id': fake.random_number()}
    }
    return order


@pytest.fixture
def get_orders_service(client, order_uri):
    response = "200"
    return response


@pytest.fixture
def create_order_with_invalid_data():
    return {'error': 'Missing required fields'}


@pytest.fixture
def get_order_by_id_with_invalid_id():
    return {'error': 'Invalid ID'}


@pytest.fixture
def get_order_by_id_with_nonexistent_id():
    return {'error': 'Order not found'}


@pytest.fixture
def get_orders_with_no_orders():
    return {'error': 'No orders found'}


@pytest.fixture
def ingredients():
    return [Ingredient(_id=1, name="Pepperoni", price=2.0), Ingredient(_id=2, name="Mushrooms", price=1.5),
            Ingredient(_id=3, name="Onions", price=1.0)]


@pytest.fixture
def beverages():
    return [Beverage(_id=1, name="Coke", price=2.5), Beverage(_id=2, name="Pepsi", price=3.5),
            Beverage(_id=3, name="Sprite", price=2.0)]
