from fastapi import FastAPI
from typing import Union 
from pydantic import BaseModel

# typing package lets you specify types, like lists, dict, set, final etc. 
# it lets you specify the type of what a variable should be
# to allow more than 1 type, have a flexible type, you use the word 'union' e.g. Union[str, none] etc.

app = FastAPI()

@app.get("/")
async def root(): # returns the root folder
    return {"message": "Hello World"}

# uvicorn main:app --reload
@app.get("/items/{item_id}") # adding a new path to the API - on the website end like the url
def read_item(item_id: int, q: Union[str, None] = None): #union[str, none] means the type can be str or none, but the = none means default value is none, so you don't have to specify it
    return {"item_id": item_id, "q": q}


# def match_regex() -> bool, the -> bool part says it's returning a boolean value
# python -m uvicorn main:app --reload potentially this will work in git bash if the normal uvicorn command doesn't work

class Item(BaseModel):
    name:str
    price:float

@app.put("/items/{item_id}") #if you define get path with same line again, i'd be overriding the previous method
def update_item(item_id:int, item: Item): #we're currently trying to use body to pass requested info
    return {"item_id": item_id, "item": item} # this is the body because it's returning it in json

# item is automatically assumed to be a body, this is because it's a complex data type, so it assumes it will be the body"
# since q on line 17 is a simple variable, it will be a path variable
# since you can only send one body, how would you send 2 items? you send a dictionary 
