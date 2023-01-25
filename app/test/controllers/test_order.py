import pytest
from app.controllers import OrderController


def test_create(app, order: dict):
    created_order, error = OrderController.create(order)
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    beverage_ids = order.pop('beverages', [])
    assert error is None
    if created_order:
        for param, value in order.items():
            assert param in created_order
            assert str(value) == created_order[param]
    assert created_order['_id']
    assert size_id == (created_order['size']['_id'])

    ingredient_ids = [int(x) for x in ingredient_ids]
    beverage_ids = [int(x) for x in beverage_ids]

    ingredients_in_detail = set(item['ingredient']['_id']
                                for item in created_order['detail'] if item['ingredient'] is not None)
    assert not ingredients_in_detail.difference(ingredient_ids)

    beverages_in_detail = set(item['beverage']['_id']
                              for item in created_order['detail'] if item['beverage'] is not None)
    assert not beverages_in_detail.difference(beverage_ids)


def test_get_by_id(app, order: dict):
    created_order, _ = OrderController.create(order)
    order_from_db, error = OrderController.get_by_id(created_order['_id'])
    size_id = order.pop('size_id', None)
    ingredient_ids = order.pop('ingredients', [])
    beverage_ids = order.pop('beverages', [])
    assert error is None
    for param, value in created_order.items():
        assert order_from_db[param] == value
    assert size_id == created_order['size']['_id']

    ingredients_in_detail = set(item['ingredient']['_id']
                                for item in created_order['detail'] if item['ingredient'] is not None)
    assert not ingredients_in_detail.difference(ingredient_ids)

    beverages_in_detail = set(item['beverage']['_id']
                              for item in created_order['detail'] if item['beverage'] is not None)
    assert not beverages_in_detail.difference(beverage_ids)


def test_get_all(app, order: dict):
    created_orders = []
    for _ in range(5):
        created_order, _ = OrderController.create(order)
        created_orders.append(created_order)

    orders_from_db, error = OrderController.get_all()
    searchable_orders = {db_order['_id']: db_order for db_order in orders_from_db}
    pytest.assume(error is None)
    for created_order in created_orders:
        current_id = created_order['_id']
        assert current_id in searchable_orders
        for param, value in created_order.items():
            pytest.assume(searchable_orders[current_id][param] == value)
