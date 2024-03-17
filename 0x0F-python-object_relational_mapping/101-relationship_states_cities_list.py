#!/usr/bin/python3
"""
Script to list all State objects and their corresponding City objects
contained in the database hbtn_0e_101_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import Base, City

if __name__ == "__main__":
    # Create a SQLAlchemy engine
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create all tables in the database
    Base.metadata.create_all(engine)
    # Create a session maker bound to the engine
    session_maker = sessionmaker(bind=engine)
    # Create a session
    session = session_maker()

    # Query all State objects and print their IDs and names
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
        # Print the IDs and names of corresponding City objects
        for city in state.cities:
            print("\t{}: {}".format(city.id, city.name))

    # Close the session and dispose of the engine
    session.close()
    engine.dispose()
