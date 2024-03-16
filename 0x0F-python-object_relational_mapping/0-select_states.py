#!/usr/bin/python3
"""This script lists all states from the database hbtn_0e_0_usa.
 Usage: ./0-select_states.py <mysql username>
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
    # Executing the SQL query to select all states
    c.execute("SELECT * FROM `states`")
    # Printing all the fetched states
    [print(state) for state in c.fetchall()]
