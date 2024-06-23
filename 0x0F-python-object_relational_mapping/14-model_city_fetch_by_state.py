#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa:
* Takes 3 arguments: mysql username, mysql password and database name
* Uses the module SQLAlchemy
* Imports State and Base from model_state - from model_state import Base, State
* Connects to a MySQL server running on localhost at port 3306
* Results are sorted in ascending order by cities.id
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]
            ),
        pool_pre_ping=True
        )
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(
        State.name,
        City.id,
        City.name
        ).join(State).order_by(City.id)
    for s in query:
        print("{}: ({}) {}".format(s[0], s[1], s[2]))
