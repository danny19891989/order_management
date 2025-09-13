import pytest
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.test import APIClient
from userauth.models import CustomUser

ORDERS_URL = "/api/v1/orders/"

def get_token(user):
    return f"Bearer {AccessToken.for_user(user)}"

def test_direct_client():
    client = APIClient()
    response = client.get("/api/v1/orders/")
    print("Status:", response.status_code)
    assert response.status_code in [401, 403, 200]

def test_unauthenticated_access(api_client):
    response = api_client.get(ORDERS_URL)
    print("Response status:", response.status_code)
    print("Response body:", response.json())
    assert response.status_code == 401

def test_customer_sees_own_orders(api_client, customer_user, create_orders):
    token = get_token(customer_user)
    api_client.credentials(HTTP_AUTHORIZATION=token)
    response = api_client.get(ORDERS_URL)
    assert response.status_code == 200
    assert all(order["customer"] == customer_user.id for order in response.json())

def test_manager_sees_all_orders(api_client, manager_user, create_orders):
    token = get_token(manager_user)
    api_client.credentials(HTTP_AUTHORIZATION=token)
    response = api_client.get(ORDERS_URL)
    assert response.status_code == 200
    assert len(response.json()) == 2  # assuming 2 orders created

def test_invalid_token(api_client):
    api_client.credentials(HTTP_AUTHORIZATION="Bearer invalidtoken123")
    response = api_client.get(ORDERS_URL)
    assert response.status_code == 401

def test_user_without_role(api_client, db):
    user = CustomUser.objects.create_user(username="norole", password="test123")
    token = get_token(user)
    api_client.credentials(HTTP_AUTHORIZATION=token)
    response = api_client.get(ORDERS_URL)
    assert response.status_code in [403, 200]  # depends on your fallback logic
