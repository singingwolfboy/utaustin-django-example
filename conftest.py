import pytest
from django.contrib.auth.models import User


@pytest.fixture
def user_client(client):
    jane = User(username="jane")
    jane.set_password("testing")
    jane.save()
    client.login(username="jane", password="testing")
    return client
