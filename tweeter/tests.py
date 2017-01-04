from django.test import Client
from django.contrib.auth.models import User
import pytest

pytestmark = pytest.mark.django_db


def test_home_page():
    c = Client()
    response = c.get("/")
    assert response.status_code == 200
    assert "Tweeter" in response.content
    assert "new user" in response.content


def test_home_page_logged_in():
    jane = User(username="jane")
    jane.set_password("testing")
    jane.save()

    c = Client()
    c.login(username="jane", password="testing")
    response = c.get("/")
    assert response.status_code == 200
    assert "jane" in response.content


def test_bad_tweet():
    jane = User(username="jane")
    jane.set_password("testing")
    jane.save()

    c = Client()
    c.login(username="jane", password="testing")
    response = c.post("/tweet", {"tweet": "This is a tweet"})
    assert response.status_code == 400


def test_tweet_not_logged_in():
    c = Client()
    response = c.post("/tweet", {"content": "This is a tweet"})
    assert response.status_code == 302
    assert response.url == '/login?next=/tweet'


def test_good_tweet():
    jane = User(username="jane")
    jane.set_password("testing")
    jane.save()

    c = Client()
    c.login(username="jane", password="testing")
    response1 = c.post("/tweet", {"content": "This is a tweet"})
    assert response1.status_code == 302
    assert response1.url == '/'

    response2 = c.get("/")
    assert response2.status_code == 200
    assert "This is a tweet" in response2.content


