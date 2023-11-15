from dto import InventoryItem, ItemOrigin
from fastapi import FastAPI
from typing import Dict

app = FastAPI() # when calling FastAPI what is it doing

my_inventory_item_dict:Dict[str, InventoryItem] = {} # currently empty dict, used to serve as a working memory
# used to look up inventory item using the serial number

@app.put("/items/{serial_num}") #naming convention inside curly braces needs to be the same as everything else in parameters for the function, the original class creation and the path
def create_item(item:InventoryItem, serial_num:str):
    my_inventory_item_dict[serial_num] = item
    print(my_inventory_item_dict)

@app.get("/items/{serial_num}") #naming convention inside curly braces needs to be the same as everything else in parameters for the function, the original class creation and the path
def read_item(serial_num: str): #union[str, none] means the type can be str or none, but the = none means default value is none, so you don't have to specify it
    return {"item":my_inventory_item_dict[serial_num]}
