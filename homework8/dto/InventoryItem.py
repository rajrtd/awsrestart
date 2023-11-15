from pydantic import BaseModel
from .ItemOrigin import ItemOrigin

class InventoryItem(BaseModel):
    name:str
    quantity: int
    serial_num:str
    origin:ItemOrigin