# app/tests/test_foo.py

import json

from django.urls import reverse


def test_hello_world():
    assert "hello_world" == "hello_world"
    assert "foo" != "bar"


def test_ping(client):
    # Given
    # client

    # When
    url = reverse("ping")
    response = client.get(url)
    content = json.loads(response.content)

    # Then
    assert response.status_code == 200
    assert content["ping"] == "pong!"