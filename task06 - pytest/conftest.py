import pytest


@pytest.fixture
def dummy_main_url():
    """
    Основная страница для тестирования API
    """
    return 'https://dummy.restapiexample.com/'


@pytest.fixture
def dummy_all_users():
    """
    Получение данных всех пользователей
    """
    return 'http://dummy.restapiexample.com/api/v1/employees'


@pytest.fixture
def dummy_add_user():
    """
    Добавление нового юзера
    """
    return 'https://dummy.restapiexample.com/api/v1/create'


@pytest.fixture
def dummy_delete_user():
    """
    Удаление пользователя по {id}
    Схема /delete/{%id%}
    """
    return 'http://dummy.restapiexample.com/api/v1/delete/'