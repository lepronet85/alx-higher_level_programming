#!/usr/bin/python3
"""
Defines a state model for SQLAlchemy ORM.

This script contains the class definition of a State
and an instance Base = declarative_base().

Attributes:
    Base: An instance of the SQLAlchemy declarative base.
    State: A class representing a state in the database.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """
    Represents a state in the MySQL table 'states'.

    Attributes:
        id (int): An auto-generated, unique integer; primary key.
        name (str): A string representing the name of the state;
        maximum length of 128 characters; cannot be null.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
