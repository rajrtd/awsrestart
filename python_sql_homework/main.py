from typing import Optional, List
from contextlib import asynccontextmanager
# One line of FastAPI imports here later &#x1f448;
from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select, delete


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    secret_name: str
    age: Optional[int] = Field(default=None, index=True)


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}" # where is the database being put

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()
    yield # yield keyword is necessary for the lifespan function to work

app = FastAPI(lifespan=lifespan)

@app.post("/heroes/")
def create_hero(hero: Hero) -> None: # why do we 
    with Session(engine) as session: # should I worry about what the 'with' and 'as' keyword do?
        session.add(hero)
        session.commit()


@app.get("/heroes/{name}")
def get_hero(name: str) -> Hero:
    with Session(engine) as session:    
        statement = select(Hero).where(Hero.name == name)
        retrieved_hero = session.exec(statement).first() # .all() does not work if there is only one hero called 'batman' for e.g. in the db, in that scenario use first        
    return retrieved_hero

@app.get("/heroes/") # response=List[Hero]
def get_heroes() -> List[Hero]:
    with Session(engine) as session:  
        statement = select(Hero).where()
        all_heroes = session.exec(statement).all()
    return all_heroes

@app.delete("/heroes/{id}")
def delete_hero(id):
     with Session(engine) as session:  
        statement = delete(Hero).where(Hero.id == id)
        session.exec(statement)
        session.commit()
