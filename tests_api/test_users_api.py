import requests
import pytest


@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"


def test_get_users_returns_list_with_required_fields(base_url):
    # endpoint API
    url = f"{base_url}/users"

    # wysłanie requestu GET
    response = requests.get(url)

    # asercja: status code
    assert response.status_code == 200

    # parsowanie JSON
    data = response.json()

    # asercja: response jest listą i nie jest pusta
    assert isinstance(data, list)
    assert len(data) > 0

    # asercje: każdy user ma wymagane pola
    for user in data:
        assert "id" in user
        assert "email" in user


def test_get_non_existing_user_returns_404(base_url):
    url = f"{base_url}/users/9999"
    response = requests.get(url)
    assert response.status_code == 404


def test_create_user_returns_201_and_id(base_url):
    url = f"{base_url}/users"

    payload = {
        "name": "API Test User",
        "username": "api_test",
        "email": "api@test.com",
    }

    response = requests.post(url, json=payload)

    # status code
    assert response.status_code == 201

    data = response.json()

    # response zawiera id
    assert "id" in data

    # response zwraca wysłane dane
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]


@pytest.mark.parametrize("user_id", [0, -1, 9999])
def test_get_invalid_user_ids_return_404(base_url, user_id):
    url = f"{base_url}/users/{user_id}"
    response = requests.get(url)
    assert response.status_code == 404
