#!/usr/bin/python3
"""
This script lists all cities from the database hbtn_0e_4_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # Creating a cursor object
    c = db.cursor()
    # Executing the SQL query to select all cities with their corresponding
    # states
    c.execute("""SELECT cities.id, cities.name, states.name
                FROM cities
                JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC""")
    # Printing all the fetched cities
    [print(city) for city in c.fetchall()]
