#!/usr/bin/python3
"""
Script to delete all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa.
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

    # Query all State objects with names containing the letter 'a'
    states = session.query(State).filter(State.name.like('%a%')).all()
    # Delete each State object found
    for state in states:
        session.delete(state)

    # Commit the changes to the database
    session.commit()
