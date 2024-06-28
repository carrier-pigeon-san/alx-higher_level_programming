#!/usr/bin/python3
"""
A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa:
* Takes 3 arguments: mysql username, mysql password and database name
* Uses the module SQLAlchemy
* Imports State and Base from model_state - from model_state import Base, State
* Connects to a MySQL server running on localhost at port 3306
* Prints the new states.id after creation
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]
            ),
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    la = State()
    la.name = "Louisiana"
    session.add(la)
    session.commit()
    query = session.query(State).filter(State.name == 'Louisiana').one()
    print("{}".format(query.id))
