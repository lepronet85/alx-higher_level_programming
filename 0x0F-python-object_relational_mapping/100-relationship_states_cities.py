#!/usr/bin/python3
"""
Script to create the State "California" with the City "San Francisco"
in the database hbtn_0e_100_usa.
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

    # Create the State "California" with the City "San Francisco"
    california = State(name="California")
    san_francisco = City(name="San Francisco", state=california)
    session.add(san_francisco)
    session.commit()
    session.close()
