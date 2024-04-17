import pytest
from django.test import TestCase
from django.urls import reverse


# Create your tests here.
def test_index_get(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


def test_donation_add_get(client):
    url = reverse('donation_add')
    response = client.get(url)
    assert response.status_code == 200


def test_login_get(client):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200


def test_login_post(client):
    url = reverse('login')
    response = client.post(url)
    assert response.status_code == 200


def test_logout_get(client):
    url = reverse('logout')
    response = client.get(url)
    assert response.status_code == 200


def test_register_get(client):
    url = reverse('register')
    response = client.get(url)
    assert response.status_code == 200
