from fastapi import FastAPI
from typing import*
from pydantic import BaseModel

class ItemOrigin(BaseModel):
    country:str
    production_date:str
    
class InventoryItem(BaseModel):
    name:str
    quantity: int
    serial_num:str
    origin:ItemOrigin

app = FastAPI()
@app.get("/")
async def root():
    pass

@app.get("/items/{serial_num}")
def read_item(my_inventory_items_dict: Dict[str, InventoryItem]):
    return {"my_inventory_items_dict": my_inventory_items_dict}

@app.put("/items/{serial_num}")
def update_item(item_origin:ItemOrigin, my_inventory_items_dict: Dict[str, InventoryItem]):
    return {"item_origin": item_origin, "my_inventory_items_dict": my_inventory_items_dict}

