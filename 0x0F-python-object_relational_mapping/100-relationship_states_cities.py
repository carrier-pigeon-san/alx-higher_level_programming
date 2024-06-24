#!/usr/bin/python3
"""
A script that creates the State “California” with the City “San Francisco”
from the database hbtn_0e_100_usa:
* Takes 3 arguments: mysql username, mysql password and database name
* Uses the module SQLAlchemy
* Connects to a MySQL server running on localhost at port 3306
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from relationship_state import State, Base
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1],
            argv[2],
            argv[3]
            ),
        pool_pre_ping=True
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    ca = State()
    ca.name = "California"
    ca.cities = [City(name="San Francisco")]

    session.add(ca)
    session.commit()
    session.close()
