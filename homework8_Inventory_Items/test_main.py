from fastapi.testclient import TestClient
from main import app

# pytest

# Looks for files names with test_*.py
# $ pytest

def test_basic_example():
    #pass
    assert(True)

#pytest command to test file and pytest -vvl

client = TestClient(app)

def test_put_api():
    response = client.put("/items/test", json = {
        "name": "first item",
        "quantity": 5,
        "serial_num": "test",
        "origin": {
            "country": "Ethiopia",
            "production_date": "2023"
        }
    })
    assert response.status_code == 200

    # to test delete call delete function but first need to call put to put there, then use get to test whether it's there, then call it's deleted
