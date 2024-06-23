#!/usr/bin/python3
"""
A script that prints the State object with the name passed as argument from
the database hbtn_0e_6_usa
* Takes 4 arguments: mysql username, mysql password, database name, and state
  name to search
* Uses the module SQLAlchemy
* Imports State and Base from model_state - from model_state import Base, State
* Connects to a MySQL server running on localhost at port 3306
* Results display the states.id
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State
from sqlalchemy.exc import NoResultFound

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]
            ),
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        q = session.query(State).filter(State.name == argv[4]).one()
    except NoResultFound:
        print("Not found")
    else:
        print("{}".format(q.id))
