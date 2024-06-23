#!/usr/bin/python3
"""
This module contains the class definition of a State and an instance
Base = declarative_base():
* State class:
  * inherits from Base Tips
  * links to the MySQL table states
  * class attribute id that represents a column of an auto-generated, unique
    integer, can’t be null and is a primary key
  * class attribute name that represents a column of a string with
    maximum 128 characters and can’t be null
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer

"""
engine = create_engine(
    'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa')
"""

Base = declarative_base()


class State(Base):
    """
    State class:
    * inherits from Base Tips
    * links to the MySQL table states
    * class attribute id that represents a column of an auto-generated, unique
      integer, can’t be null and is a primary key
    * class attribute name that represents a column of a string with
      maximum 128 characters and can’t be null
    """

    __tablename__ = 'states'

    id = Column(Integer, unique=True, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)


# Base.metadata.create_all(engine)
