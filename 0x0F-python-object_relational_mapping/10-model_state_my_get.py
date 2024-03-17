#!/usr/bin/python3
"""
Script to print the State object with the name passed as
an argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    # Create a session maker bound to the engine
    session_maker = sessionmaker(bind=engine)
    # Create a session
    session = session_maker()

    # Iterate through all State objects and print the ID of
    # the one with the specified name
    for state in session.query(State):
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")
