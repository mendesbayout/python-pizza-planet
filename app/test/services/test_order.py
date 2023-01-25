def test_create_order_service(create_order):
    order = create_order
    assert 'client_name' in order, 'Order should have a client name'
    assert 'client_dni' in order, 'Order should have a client DNI'
    assert 'ingredients' in order, 'Order should have ingredients'
    assert 'beverages' in order, 'Order should have beverages'
    assert 'size_id' in order, 'Order should have size_id'


def test_get_order_by_id_service(get_order_by_id_service):
    order = get_order_by_id_service
    assert order['_id'], 'Order should have an _id'
    assert order['client_name'], 'Order should have a client name'
    assert order['client_dni'], 'Order should have a client DNI'
    assert order['client_address'], 'Order should have a client address'
    assert order['client_phone'], 'Order should have a client phone number'
    assert order['date'], 'Order should have a date'
    assert order['total_price'], 'Order should have a total price'
    assert order['size']['_id'], 'Order should have a size'
    assert order['size'], 'Order should have a size'


def test_create_order_with_invalid_data(create_order_with_invalid_data):
    assert create_order_with_invalid_data == {'error': 'Missing required fields'}, 'Unexpected error message'


def test_get_order_by_id_with_invalid_id(get_order_by_id_with_invalid_id):
    assert get_order_by_id_with_invalid_id == {'error': 'Invalid ID'}, 'Unexpected error message'


def test_get_order_by_id_with_nonexistent_id(get_order_by_id_with_nonexistent_id):
    assert get_order_by_id_with_nonexistent_id == {'error': 'Order not found'}, 'Unexpected error message'


def test_get_orders_with_no_orders(get_orders_with_no_orders):
    assert get_orders_with_no_orders == {'error': 'No orders found'}, 'Unexpected error message'
