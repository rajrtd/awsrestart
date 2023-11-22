from typing import Optional
from fastapi import FastAPI
from sqlmodel import Field, SQLModel, Session, create_engine, select


app = FastAPI()


class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)

engine = create_engine("sqlite:///database.db")

SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(hero_1)
#     session.add(hero_2)
#     session.add(hero_3)
#     session.commit()

with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "Spider-Boy")
    heros = session.exec(
        statement
    ).all()  # since we have 2 entries, just get the first entry, to print all heros that are named spider-boy use all()
    print(heros)
    print(type(heros))
    hero = session.exec(statement).first()
    print(hero)

# @app.put("/")
# def put_api():

from typing import Optional

# One line of FastAPI imports here later &#x1f448;
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


@app.on_event("startup")
def on_startup():
    create_db_and_tables()


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


# hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
# hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
# hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)


# engine = create_engine("sqlite:///database.db")


# SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(hero_1)
#     session.add(hero_2)
#     session.add(hero_3)
#     session.commit()

# with Session(engine) as session:
#     statement = select(Hero).where(Hero.name == "Spider-Boy")
#     heroes = session.exec(statement).all() #returns list of all records that match
#     print(heroes)
#     print(type(heroes))
#     hero = session.exec(statement).first() #returns only first record
#     print(hero)
