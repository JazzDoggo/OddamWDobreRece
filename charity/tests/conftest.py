import pytest
from django.test import Client


@pytest.fixture
def client():
    client = Client()
    return client


@pytest.fixture
def fix_user_data():
    data = {
        'first_name': 'Test',
        'last_name': 'Test',
        'email': 'test@test.com',
        'password': 'Test',
        'password2': 'Test',
    }
