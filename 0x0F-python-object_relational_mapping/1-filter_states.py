#!/usr/bin/python3
"""This script lists all states with a name starting with 'N' (uppercase)
 from the database hbtn_0e_0_usa.
 Usage: ./1-filter_states.py <mysql username>
                            <mysql password>
                            <database name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # Creating a cursor object
    c = db.cursor()
    # Executing the SQL query to select all states and ordering by ID
    c.execute("SELECT * FROM `states` ORDER BY `id`")
    # Printing states whose names start with 'N'
    [print(state) for state in c.fetchall() if state[1][0] == "N"]
