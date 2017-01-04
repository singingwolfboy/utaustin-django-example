import pytest

@pytest.mark.django_db
def test_home_page(client):
    resp = client.get("/")
    assert resp.status_code == 200
    assert "form" in resp.context
    assert "recent_tweets" in resp.context

