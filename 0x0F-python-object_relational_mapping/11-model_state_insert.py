#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa """

from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    new_id = 0
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        new_id = instance.id
    new_id = new_id + 1
    new_state = State(name="Louisiana", id=new_id)
    session.add(new_state)
    session.commit()
    print(new_state.id)
