#!/usr/bin/python3
"""
This module contains the class definition of a City and an instance
* City class:
  * inherits from Base (imported from model_state)
  * links to the MySQL table cities
  * class attribute id that represents a column of an auto-generated, unique
    integer, can’t be null and is a primary key
  * class attribute name that represents a column of a string with
    maximum 128 characters and can’t be null
  * class attribute state_id that represents a column of an integer, can’t be
    null and is a foreign key to states.id
"""
from model_state import State, Base
from sqlalchemy import Column, String, Integer, ForeignKey


class City(Base):
    """
    City class:
    * inherits from Base (imported from model_state)
    * links to the MySQL table cities
    * class attribute id that represents a column of an auto-generated, unique
      integer, can’t be null and is a primary key
    * class attribute name that represents a column of a string with
      maximum 128 characters and can’t be null
    * class attribute state_id that represents a column of an integer, can’t
      be null and is a foreign key to states.id
    """

    __tablename__ = 'cities'

    id = Column(Integer, unique=True, primary_key=True, autoincrement=True,
                nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
