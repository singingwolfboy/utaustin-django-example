from django.test import Client
from django.contrib.auth.models import User
import pytest

@pytest.mark.django_db
def test_home_page():
    c = Client()
    response = c.get("/")
    assert response.status_code == 200
    assert "Tweeter" in response.content
    assert "new user" in response.content


@pytest.mark.django_db
def test_home_page_logged_in():
    jane = User(username="jane")
    jane.set_password("testing")
    jane.save()

    c = Client()
    c.login(username="jane", password="testing")
    response = c.get("/")
    assert response.status_code == 200
    assert "jane" in response.content
