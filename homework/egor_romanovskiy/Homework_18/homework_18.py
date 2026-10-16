import requests


def get_all_objects():
    response = requests.get(url='http://objapi.course.qa-practice.com/object')
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    assert len(response.json()['data']) > 0, 'No objects returned in response'


def get_object():
    object_id = new_object_id()
    response = requests.get(url=f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    response_json = response.json()
    assert response_json['id'] == object_id, f"Expected id = {object_id} in response but was {response_json['id']}"
    clear(object_id)


def create_object(name, color, size):
    body = {'data': {'color': color, 'size': size}, 'name': name}
    response = requests.post(url='http://objapi.course.qa-practice.com/object', json=body)
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    response_json = response.json()
    assert response_json['name'] == name, f"Expected name {name} but was {response_json['name']}"
    assert response_json['data']['color'] == color, f"Expected color {color} but was {response_json['data']['color']}"
    assert response_json['data']['size'] == size, f"Expected size {size} but was {response_json['data']['size']}"
    clear(response_json['id'])


def put_object(name, color, size):
    object_id = new_object_id()
    body = {'data': {'color': color, 'size': size}, 'id': object_id, 'name': name}
    response = requests.put(url=f'http://objapi.course.qa-practice.com/object/{object_id}', json=body)
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    response_json = response.json()
    assert response_json['name'] == name, f"Expected name {name} but was {response_json['name']}"
    assert response_json['data']['color'] == color, f"Expected color {color} but was {response_json['data']['color']}"
    assert response_json['data']['size'] == size, f"Expected size {size} but was {response_json['data']['size']}"
    clear(object_id)


def patch_object():
    object_id = new_object_id()
    body = {'data': {'color': 'color_patched'}, 'name': 'name_patched'}
    response = requests.patch(url=f'http://objapi.course.qa-practice.com/object/{object_id}', json=body)
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    response_json = response.json()
    assert response_json['name'] == 'name_patched', f"Expected 'name_patched' but was {response_json['name']}"
    assert response_json['data']['color'] == 'color_patched', \
        f"Expected 'color_patched' but was {response_json['data']['color']}"
    clear(object_id)


def delete_object():
    object_id = new_object_id()
    response = requests.delete(url=f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'
    assert check_object_by_id(object_id) == 404, f'Expected status code 404 but was {check_object_by_id(object_id)}'


def clear(object_id):
    response = requests.delete(url=f'http://objapi.course.qa-practice.com/object/{object_id}')
    assert response.status_code == 200, f'Expected status code 200 but was {response.status_code}'


def new_object_id():
    body = {'data': {'color': 'color', 'size': 'size'}, 'name': 'name'}
    response = requests.post(url='http://objapi.course.qa-practice.com/object', json=body)
    return response.json()['id']


def check_object_by_id(object_id):
    response = requests.get(url=f'http://objapi.course.qa-practice.com/object/{object_id}')
    return response.status_code


get_all_objects()
get_object()
create_object('my object', 'red', 'small')
put_object('name_upd', 'color_upd', 'size_upd')
patch_object()
delete_object()
