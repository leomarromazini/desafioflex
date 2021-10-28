import json
from app import create_app

app = create_app()

test_client = app.test_client()


def test_if_route_files_accepts_get_request():

    assert "GET" in (test_client.options("/certificate").headers["Allow"])


def test_files_route_does_not_accepts_put_request():

    assert test_client.put("/certificate").status_code == 405


def test_if_route_certificate_accepts_post_request():

    assert "POST" in (test_client.options("/certificate").headers["Allow"])


def test_if_route_get_certificate_status_code_is_200():
    response = test_client.get("/certificate")
    assert response.status_code == 200


def test_if_route_post_certificate_status_code_is_201():

    data = {
        "name": "test",
        "username": "test",
        "description": "test",
        "groups": [1, 15],
        "expiration": 20,
    }

    response = test_client.post("/certificate", data=json.dumps(data), headers={"Content-Type": "application/json"})
    
    assert response.status_code == 201

