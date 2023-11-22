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

# with Session(engine) as session:
#     statement = select(Hero).where(Hero.name == "Spider-Boy")
#     heros = session.exec(
#         statement
#     ).all()  # since we have 2 entries, just get the first entry, to print all heros that are named spider-boy use all()
#     print(heros)
#     print(type(heros))
#     hero = session.exec(statement).first()
#     print(hero)
    
# hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
# hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
# hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
# test_hero = Hero(name="The Flash", secret_name = "Barry Allen")

engine = create_engine("sqlite:///database.db")


SQLModel.metadata.create_all(engine)

# with Session(engine) as session:
#     session.add(test_hero)
#     session.commit()

# with Session(engine) as session:
#     statement = select(Hero).where(Hero.name == "Spider-Boy")
#     heroes = session.exec(statement).all() #returns list of all records that match
#     print(heroes)
#     print(type(heroes))
#     hero = session.exec(statement).first() #returns only first record
#     print(hero)

# testing 
with Session(engine) as session:
    statement = select(Hero).where(Hero.name == "The Flash")
    hero = session.exec(statement)