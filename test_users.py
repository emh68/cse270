import requests

BASE_URL = "http://127.0.0.1:8000/users/"

def test_login_valid_user():
    """Test that a valid username/password returns HTTP 200"""
    params = {"username": "admin", "password": "qwerty"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"


def test_login_invalid_user():
    """Test that an invalid username/password returns HTTP 401"""
    params = {"username": "admin", "password": "admin"}
    response = requests.get(BASE_URL, params=params)
    assert response.status_code == 401, f"Expected 401, got {response.status_code}"