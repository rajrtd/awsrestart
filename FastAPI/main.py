from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root(): # returns the root
    return {"message": "Hello World"}