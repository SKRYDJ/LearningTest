'''
Работу поместить в файл test_task06.py и разместить его в репозитории.

Протестировать API.
Можно взять одно из двух на выбор:
https://dummy.restapiexample.com/
https://reqres.in/


Необходимо написать не менее пяти тестов.
Протестировать как методы GET так и пост POST.
При создании тестов использовать фикстуры.
'''
import json
import pytest
import requests
from pydantic import BaseModel


class DummyModel(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str
    url: str
    text: str


@pytest.mark.checksingleuser
def test_get(dummy_single_user):
    resp_get = requests.get(dummy_single_user + str(2))
    assert resp_get.status_code == requests.codes.ok
    assert DummyModel(**resp_get.json())


@pytest.mark.checkadduser
def test_create_user(dummy_add_user, user_data):
    crt_user = requests.post(dummy_add_user, json=user_data)
    assert crt_user.status_code == 201


@pytest.mark.deleteuser
def test_delete_user_by_id(dummy_all_users, dummy_delete_user):
    response = requests.get(dummy_all_users).json()
    dict_json = json.dumps(response)
    if 'Janet' in dict_json:
        del_user_req = requests.delete(dummy_delete_user + '2')
        assert del_user_req.status_code == 204
    else:
        print('Name Janet does not exist')


new_user_data = [(1, 'george.bluth@reqres.in', 'George', 'Bluth', 'https://reqres.in/img/faces/1-image.jpg'),
                 (2, 'janet.weaver@reqres.in', 'Janet', 'Weaver', 'https://reqres.in/img/faces/2-image.jpg')
                 ]


@pytest.mark.parametrize('user_id, email, first_name, last_name, avatar', new_user_data)
def test_param_user(dummy_single_user, user_id, email, first_name, last_name, avatar):
    param_user = requests.get(dummy_single_user + str(user_id)).json()
    assert param_user['data']['email'] == email
    assert param_user['data']['first_name'] == first_name
