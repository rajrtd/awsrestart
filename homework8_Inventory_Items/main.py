from dto import InventoryItem, ItemOrigin
from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI() # when calling FastAPI what is it doing?

my_inventory_item_dict:Dict[str, InventoryItem] = {} # currently empty dict, used to serve as a working memory
# used to look up inventory item using the serial number

@app.put("/items/{serial_num}") #naming convention inside curly braces needs to be the same as everything else in parameters for the function, the original class creation and the path
def create_item(item:InventoryItem, serial_num:str) -> None:
    my_inventory_item_dict[serial_num] = item

@app.get("/items/{serial_num}") #naming convention inside curly braces needs to be the same as everything else in parameters for the function, the original class creation and the path
def read_item(serial_num: str) -> InventoryItem: #union[str, none] means the type can be str or none, but the = none means default value is none, so you don't have to specify it
    if serial_num in my_inventory_item_dict.keys():
        return my_inventory_item_dict[serial_num]
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    
@app.delete("/items/{serial_num}")
def delete_item(serial_num:str) -> Dict:
      if serial_num in my_inventory_item_dict.keys():
        my_deleted_item = my_inventory_item_dict.pop(serial_num)
        print(my_inventory_item_dict)
        return {"msg": "item {my_deleted_item} is successfully deleted"}
      else:
        raise HTTPException(status_code=404, detail="Item not found")

@app.get("/items/") 
def get_item() -> List[InventoryItem]: # -> List[InventoryItem] I've specified what this function is returning
    return my_inventory_item_dict.values() # getting a list of values

