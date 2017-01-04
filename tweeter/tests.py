from django.test import Client
import pytest

@pytest.mark.django_db
def test_home_page():
    c = Client()
    response = c.get("/")
    assert response.status_code == 200
    assert "Tweeter" in response.content
    # pytest.set_trace()
