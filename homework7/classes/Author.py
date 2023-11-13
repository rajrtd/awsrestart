from pydantic import BaseModel

class Author(BaseModel):
    name:str
    author_id:str

    def check_valid_name(cls, name:str):
        nameList = list(name)
        nameList[0].capitalize()
        nameChecker:bool
        nameChecker = True

        for index in range(len(nameList)):
            spaceCount = 0

            if(nameList[index] == " "):
                spaceCount += 1
                nameList[index + 1] = nameList[index + 1].capitalize()
                nameChecker = True
            
            if(spaceCount > 2):
                nameChecker = False
                break
        
        assert nameChecker, "There is more than a first name and surname provided"
        return name

        

