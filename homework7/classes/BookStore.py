from pydantic import BaseModel
from .BookItem import BookItem

class BookStore(BaseModel):
    name:str
    book_shelve:list[BookItem]    