"""
Работу поместить в файл test_task06.py и разместить его в репозитории.

Протестировать API.
Можно взять одно из двух на выбор:
https://dummy.restapiexample.com/
https://reqres.in/


Необходимо написать не менее пяти тестов.
Протестировать как методы GET так и пост POST.
При создании тестов использовать фикстуры.
"""

import pytest
import requests
from pydantic import BaseModel


class DummyModel(BaseModel):
    name: str
    salary: int
    age: int
    id: int


def test_get():
    respGet = requests.get()
    assert respGet.status_code == requests.codes.ok
    assert DummyModel(**respGet.json())


def test_single_user_not_found(new_value):
    assert new_value == "hello Sergio"
    #assert new_value == "hell Sergio"
