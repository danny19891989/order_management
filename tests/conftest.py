import pytest
from rest_framework.test import APIClient
from userauth.models import CustomUser
from orders.models import Order

@pytest.fixture
def api_client():
    return APIClient()

@pytest.fixture
def customer_user(db):
    return CustomUser.objects.create_user(username="customer1", password="danny1234", role="customer")

@pytest.fixture
def manager_user(db):
    return CustomUser.objects.create_user(username="manager1", password="admin1234", role="manager")

@pytest.fixture
def create_orders(customer_user, manager_user):
    Order.objects.create(customer=customer_user, total_amount=100, total_price=100.00)
    Order.objects.create(customer=manager_user, total_amount=200, total_price=100.00)
