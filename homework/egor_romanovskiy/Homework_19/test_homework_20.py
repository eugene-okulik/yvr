import requests
import pytest


@pytest.fixture()
def new_object_id():
    body = {'data': {'color': 'color', 'size': 'size'}, 'name': 'name'}
    response = requests.post(url='http://objapi.course.qa-practice.com/object', json=body)
    object_id = response.json()['id']
    yield object_id
    requests.delete(url=f'http://objapi.course.qa-practice.com/object/{object_id}')


@pytest.fixture(scope='session')
def start_end_session():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(autouse=True)
def before_after_test():
    print('before test')
    yield
    print('after test')


def check_object_by_id(object_id):
    response = requests.get(url=f'http://objapi.course.qa-practice.com/object/{object_id}')
    return response.status_code


@pytest.mark.medium
def test_get_all_objects(start_end_session):
    response = requests.get(url='http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    assert len(response.json()['data']) > 0, 'No objects returned in response'


@pytest.mark.critical
def test_get_object(new_object_id):
    response = requests.get(url=f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    response_json = response.json()
    assert response_json['id'] == new_object_id, \
        f"Expected id = {new_object_id} in response but was {response_json['id']}"


@pytest.mark.parametrize(
    'name, color, size',
    [
        ('first', 'red', 'small'),
        ('second', 'green', 'medium'),
        ('third', 'yellow', 'big')
    ]
)
def test_create_object(name, color, size):
    body = {'data': {'color': color, 'size': size}, 'name': name}
    response = requests.post(url='http://objapi.course.qa-practice.com/object', json=body)
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    response_json = response.json()
    assert response_json['name'] == name, f"Expected name {name} but was {response_json['name']}"
    assert response_json['data']['color'] == color, f"Expected color {color} but was {response_json['data']['color']}"
    assert response_json['data']['size'] == size, f"Expected size {size} but was {response_json['data']['size']}"
    requests.delete(url=f"http://objapi.course.qa-practice.com/object/{response_json['id']}")


def test_put_object(new_object_id):
    body = {'data': {'color': 'red', 'size': 'big'}, 'id': new_object_id, 'name': 'third'}
    response = requests.put(url=f'http://objapi.course.qa-practice.com/object/{new_object_id}', json=body)
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    response_json = response.json()
    assert response_json['name'] == 'third', f"Expected name 'third' but was {response_json['name']}"
    assert response_json['data']['color'] == 'red', f"Expected color 'red' but was {response_json['data']['color']}"
    assert response_json['data']['size'] == 'big', f"Expected size 'big' but was {response_json['data']['size']}"


def test_patch_object(new_object_id):
    body = {'data': {'color': 'color_patched'}, 'name': 'name_patched'}
    response = requests.patch(url=f'http://objapi.course.qa-practice.com/object/{new_object_id}', json=body)
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    response_json = response.json()
    assert response_json['name'] == 'name_patched', f"Expected 'name_patched' but was {response_json['name']}"
    assert response_json['data']['color'] == 'color_patched', \
        f"Expected 'color_patched' but was {response_json['data']['color']}"


def test_delete_object(new_object_id):
    response = requests.delete(url=f'http://objapi.course.qa-practice.com/object/{new_object_id}')
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    assert check_object_by_id(new_object_id) == 404, \
        f'Expected status code 404 but was {check_object_by_id(new_object_id)}'
