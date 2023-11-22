from typing import Optional

# One line of FastAPI imports here later &#x1f448;
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

app = FastAPI()

async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield


@app.post("/heroes/")
def create_hero(hero: Hero):
    # implement part 1 here
    pass


@app.get("/heroes/{name}")
def get_hero(name: str):
    # implement part 2 here
    pass


@app.get("/heroes/")
def get_heroes():
    # implement part 3 here
    pass