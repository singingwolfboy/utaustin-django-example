import pytest
from django.contrib.auth.models import User
from tweeter.models import Tweet

pytestmark = pytest.mark.django_db


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


def test_empty_search(client):
    response = client.get("/search/")
    assert response.status_code == 200
    assert "<input" in response.content
    assert "Search" in response.content


def test_search_no_results(client):
    response = client.get("/search/query")
    assert response.status_code == 200
    assert "No search results. Sorry!" in response.content


def test_search_with_result(client):
    user = User(username="bob_ross")
    user.save()
    tweet = Tweet(content="happy little trees", creator=user)
    tweet.save()

    response = client.get("/search/trees")
    assert response.status_code == 200
    assert "happy little trees" in response.content
    assert "@bob_ross" in response.content


def test_search_by_user(client):
    user1 = User(username="bob_ross")
    user1.save()
    tweet1 = Tweet(content="happy little trees", creator=user1)
    tweet1.save()
    user2 = User(username="lorax")
    user2.save()
    tweet2 = Tweet(
        content="I am the Lorax. I speak for the trees.",
        creator=user2,
    )
    tweet2.save()

    response = client.get("/search/trees user:bob_ross")
    assert response.status_code == 200
    assert "@bob_ross" in response.content
    assert "happy little trees" in response.content
    assert "@lorax" not in response.content
    assert "I am the Lorax" not in response.content


def test_search_bad_user(client):
    response = client.get('/search/user:nonexistant foo')
    assert response.status_code == 200
    assert (
        "One or more of the users in your query does not exist."
        in response.content
    )
    assert "No search results. Sorry!" not in response.content






