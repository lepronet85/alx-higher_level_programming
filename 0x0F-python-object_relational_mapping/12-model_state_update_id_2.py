#!/usr/bin/python3
"""
Script to update the name of the State object with id=2 in the
database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State

if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create a session maker bound to the engine
    session_maker = sessionmaker(bind=engine)
    # Create a session
    session = session_maker()

    # Query the State object with id=2 and update its name to "New Mexico"
    state = session.query(State).filter_by(id=2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
    else:
        print("State with id=2 not found")
