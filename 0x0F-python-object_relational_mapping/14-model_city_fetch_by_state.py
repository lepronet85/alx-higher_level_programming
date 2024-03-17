#!/usr/bin/python3
"""
Script to print all City objects from the database hbtn_0e_14_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
from model_city import City

if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create a session maker bound to the engine
    session_maker = sessionmaker(bind=engine)
    # Create a session
    session = session_maker()

    # Query and print all City objects along with their corresponding
    # State names
    for city, state in session.query(City, State)\
        .filter(City.state_id == State.id)\
            .order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
