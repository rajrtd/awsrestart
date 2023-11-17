from fastapi.testclient import TestClient
from main import app
from typing import Dict

# pytest

# Looks for files names with test_*.py
# $ pytest

#pytest command to test file and pytest -vvl

client = TestClient(app)

myDict:Dict = {
        "name": "first item",
        "quantity": 5,
        "serial_num": "test",
        "origin": {
            "country": "Ethiopia",
            "production_date": "2023"
        }} #input that is given to API is expected in a dictionary format/json format that's why it needs to be a dictionary

myIncorrectDict:Dict = {
        "name": "first item",
        "quantity": "A",
        "serial_num": "test",
        "origin": {
            "country": "Ethiopia",
            "production_date": "2023"
        }} 

def test_put_api(): 
    response = client.put("/items/test/", json = myDict)
    assert response.status_code == 200 
    # to test delete call delete function but first need to call put to put there, then use get to test whether it's there, then call it's deleted

def test_incorrect_input_put_api(): 
    response = client.put("/items/test/", json = myIncorrectDict)
    # print(response.json()) - can print out using pytest -vvl flag will print out when test fails
    assert response.status_code == 422
    assert "Input should be a valid integer, unable to parse string as an integer" in str(response.json()) # status 422 error  
    
def test_get_api(): 
    response = client.get("/items/test/")
    assert response.status_code == 200 and response.json() == myDict

# def test_get_all_api(): 
#     response = client.get("/items/")
#     assert response.status_code == 200

# def test_delete_api():
#     response = client.delete("items/test/")
#     assert response.status_code == 200

# def test_confirm_delete_api():
#     response = client.get("/items/test/")
#     assert response.status_code == 404