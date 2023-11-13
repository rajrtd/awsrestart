from pydantic import BaseModel, field_validator

class Author(BaseModel):
    name:str
    author_id:str
    
    @field_validator("name")
    def check_valid_name(cls, name:str):
        assert name.istitle(), "Name is invalid"
        return name

        

