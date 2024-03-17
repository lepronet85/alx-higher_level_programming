#!/usr/bin/python3
"""
Script to retrieve the first State object from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]),
        pool_pre_ping=True)
    # Create a session maker bound to the engine
    session_maker = sessionmaker(bind=engine)
    # Create a session
    session = session_maker()

    # Retrieve the first State object ordered by its ID
    state = session.query(State).order_by(State.id).first()
    # Print the State object if found, otherwise print "Nothing"
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
