import pytest
import json
import requests


@pytest.fixture
def dummy_single_user():
    """
    Получение данных одного пользователя
    """
    return 'https://reqres.in/api/users/'


@pytest.fixture
def dummy_all_users():
    """
    Получение данных всех пользователей
    """
    return 'https://reqres.in/api/users'


@pytest.fixture
def dummy_add_user():
    """
    POST Добавление нового юзера
    """
    return 'https://reqres.in/api/users'


@pytest.fixture
def dummy_delete_user():
    """
    Удаление пользователя по {id}
    Схема /delete/{%id%}
    """
    return 'https://reqres.in/api/users/'

@pytest.fixture
def dummy_log_in():
    """
    Станица логина
    """
    return 'https://reqres.in/api/login'

@pytest.fixture
def dict_all_user_data():
    response = requests.get('https://reqres.in/api/users/').json()
    dict_json = json.dumps(response)
    return dict_json


@pytest.fixture
def user_data():
    use_data = [(1, 'george.bluth@reqres.in', 'George', 'Bluth', 'https://reqres.in/img/faces/1-image.jpg'),
                (2, 'janet.weaver@reqres.in', 'Janet', 'Weaver', 'https://reqres.in/img/faces/2-image.jpg')
                ]
    return use_data

