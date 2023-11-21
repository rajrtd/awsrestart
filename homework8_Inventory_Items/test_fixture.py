from fastapi.testclient import TestClient
from main import app
import pytest  # imports everything from pytest


@pytest.fixture
def client():  # every time a client fixture is referenced it will create a new test client
    yield TestClient(app)  # yield is equivalent to return, with some differences


# To use GET/DELETE API, PUT api needs to get used first - code repetition.
# 1) Fixture = precondition to test case. Pre-initialization of an object and return it
# 2) Providing a matrix of inputs and receiving a matrix of outputs
# 3) Mock - blackbox testing


@pytest.fixture
def good_payload():
    return {
        "name": "first item",
        "quantity": 5,
        "serial_num": "test",
        "origin": {"country": "Ethiopia", "production_date": "2023"},
    }


@pytest.fixture
def bad_payload():
    return {
        "name": "first item",
        "quantity": "A",  # the incorrect input
        "serial_num": "test",
        "origin": {"country": "Ethiopia", "production_date": "2023"},
    }


def test_incorrect_input_put_api(
    client, bad_payload
):  # how is it getting access to the data in the bad_payload() function? Because it's a test fixture, text fixtures allows you to do that
    response = client.put("/items/test/", json=bad_payload)
    assert response.status_code == 422
    assert (
        "Input should be a valid integer, unable to parse string as an integer"
        in str(response.json())
    )


def test_get_api(
    client,
):  # Client is new every time it is passed as a test fixture in a test function
    response = client.get(
        "/items/test/"
    )  # it was referring to the test_main.py's put function so it could use get successfully
    assert response.status_code == 404


def test_put_then_get_api(client, good_payload):
    response = client.put("/items/test/", json=good_payload)
    assert response.status_code == 200
    response = client.get(f"/items/test/")
    assert response.status_code == 200 and response.json() == good_payload


# parametrize allows you to put thru many test cases at once, include parameter names as strings
# first test case a = 1, b = 2, expected = 3
# second test case a = 5, b = -1, expected = 4
@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3), (5, -1, 4), (3, 3, 6)],
)
def test_addition(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize(
    "payload, http_code",
    [
        (
            {
                "name": "first item",
                "quantity": 5,
                "serial_num": "test",
                "origin": {"country": "Ethiopia", "production_date": "2023"},
            },
            200,
        ),
        (
            {
                "name": "first item",
                "quantity": "A",  # the incorrect input
                "serial_num": "test",
                "origin": {"country": "Ethiopia", "production_date": "2023"},
            },
            422,
        ),
    ],
    # indirect=[
    #     "payload"
    # ],  # indirectly saying we're evaluating the good payload and bad payload
)
def test_many_put_apis(client, payload, http_code):
    assert client.put("/items/test/", json=payload).status_code == http_code
