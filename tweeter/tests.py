from django.test import Client
from django.contrib.auth.models import User
import pytest

pytestmark = pytest.mark.django_db


@pytest.fixture
def user_client(client):
    jane = User(username="jane")
    jane.set_password("testing")
    jane.save()
    client.login(username="jane", password="testing")
    return client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert "Tweeter" in response.content
    assert "new user" in response.content


def test_home_page_logged_in(user_client):
    response = user_client.get("/")
    assert response.status_code == 200
    assert "jane" in response.content


def test_bad_tweet(user_client):
    response = user_client.post("/tweet", {"tweet": "This is a tweet"})
    assert response.status_code == 400


def test_tweet_not_logged_in(client):
    response = client.post("/tweet", {"content": "This is a tweet"})
    assert response.status_code == 302
    assert response.url == '/login?next=/tweet'


def test_good_tweet(user_client):
    response1 = user_client.post("/tweet", {"content": "This is a tweet"})
    assert response1.status_code == 302
    assert response1.url == '/'

    response2 = user_client.get("/")
    assert response2.status_code == 200
    assert "This is a tweet" in response2.content
