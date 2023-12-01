from typing import Optional, List
from contextlib import asynccontextmanager
# One line of FastAPI imports here later &#x1f448;
from fastapi import FastAPI, HTTPException
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

# new way to do DTO, it defines the payload when you want to have an update operation
class HeroUpdate(SQLModel): # specialized class for each database operation Create Read Update Delete. 
    name:Optional[str] = None
    secret_name: Optional[str] = None
    age:Optional[int] = None

@app.patch("/hero/", response_model=Hero) # if you want to change more than one piece of data is by create and customize a hero model. The way to do it is create another sql model, and it's only used to change existing the DAO in the database
def change_secret_name(hero_update:HeroUpdate):
    with Session(engine) as session:
        db_hero = session.get(Hero, hero_update.name).first() #.one() can be used but that is a syntax from sqlalchemy
        if not db_hero:
            raise HTTPException(status_code=404, detail="Hero not found")
    

@app.get("/heroes/{name}", response_model=Hero)
def get_hero(name: str) -> Hero:
    with Session(engine) as session:    
        statement = select(Hero).where(Hero.name == name)
        retrieved_hero = session.exec(statement).first() # .all() does not work if there is only one hero called 'batman' for e.g. in the db, in that scenario use first        
    return retrieved_hero

@app.get("/heroes/", response_model=List[Hero])
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

#pydantic usually automatically does the typehinting for the output of our function, but since we're not using pydantic here
# we need to specify the response