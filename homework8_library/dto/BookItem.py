from pydantic import BaseModel
from .Author import Author

class BookItem(BaseModel):
    name:str
    author:Author
    year_published:int

    def check_valid_year(cls, year:str):
        assert year >= 3000 and year <= 2023, "Year published must be greater than -3000 and less than 2023"
        return year

