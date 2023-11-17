from dto import Author, BookItem, BookStore
from fastapi import FastAPI, HTTPException
from typing import Dict, List

app = FastAPI()

myBookItemsDict:Dict[str, BookItem] = {} # is this the syntax for key, value dictionaries?

@app.put("/books/{name}")
def createBook(book:BookItem, name:str) -> None:
    myBookItemsDict[name] = book
    print(myBookItemsDict.keys())

@app.get("/books/{name}")
def readBook(name: str) -> BookItem:
    if name in myBookItemsDict.keys():
        return myBookItemsDict[name]
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@app.delete("/books/{name}")
def deleteBook(name:str) -> Dict:
    if name in myBookItemsDict.keys():
        myBookItemsDict.pop(name)
        return {"message": "Item is successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="Book not found")

@app.get("/books/")
def getBooks() -> List[BookItem]:
    return myBookItemsDict.values()
