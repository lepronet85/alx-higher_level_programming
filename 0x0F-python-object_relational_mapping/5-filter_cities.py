#!/usr/bin/python3
"""
This script lists all cities of a given state using the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # Creating a cursor object
    c = db.cursor()
    # Executing the SQL query to select all cities of the specified state
    c.execute("""SELECT * FROM cities
                INNER JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id""")
    # Extracting and joining the names of cities belonging to the specified state
    cities_of_state = [city[2] for city in c.fetchall() if city[4] == sys.argv[4]]
    print(", ".join(cities_of_state))
