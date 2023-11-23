from typing import Optional, List
from contextlib import asynccontextmanager
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


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield # yield keyword is necessary for the app to run

app = FastAPI(lifespan=lifespan)

@app.post("/heroes/")
def create_hero(hero: Hero) -> None:
    with Session(engine) as session:
        session.add(hero)
        session.commit()


@app.get("/heroes/{name}")
def get_hero(name: str) -> Hero:
    with Session(engine) as session:    
        statement = select(Hero).where(Hero.name == name)
        retrieved_hero = session.exec(statement).all()        
    return retrieved_hero

@app.get("/heroes/") # response=List[Hero]
def get_heroes() -> List[Hero]:
    with Session(engine) as session:  
        statement = select(Hero).where()
        all_heroes = session.exec(statement).all()
    return all_heroes