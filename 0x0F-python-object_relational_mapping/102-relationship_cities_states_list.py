#!/usr/bin/python3
""" lists all City objects from the database hbtn_0e_101_usa """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from relationship_state import State
from relationship_city import Base, City
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for estado in session.query(State).order_by(State.id):
        for city in estado.cities:
            print(city.id, end="")
            print(":", city.name, end="")
            print(" ->", estado.name)
