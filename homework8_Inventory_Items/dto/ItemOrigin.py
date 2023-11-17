from pydantic import BaseModel

class ItemOrigin(BaseModel):
    country:str
    production_date:str