#!/usr/bin/python3
"""
Defines a City model for SQLAlchemy ORM.

This script contains the class definition of a City
and an instance Base = declarative_base().

Attributes:
    Base: An instance of the SQLAlchemy declarative base.
    City: A class representing a city in the database.
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Represents a city in the MySQL table 'cities'.

    Attributes:
        id (int): An auto-generated, unique integer; primary key.
        name (str): A string representing the name of the city;
        maximum length of 128 characters; cannot be null.
        state_id (int): An integer representing the foreign key to
        the 'states' table; cannot be null.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
