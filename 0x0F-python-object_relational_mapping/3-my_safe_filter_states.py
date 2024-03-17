#!/usr/bin/python3
"""
This script displays all values in the states table of hbtn_0e_0_usa
where the name matches the argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    # Creating a cursor object
    c = db.cursor()
    # Executing the SQL query to select all states
    c.execute("""SELECT * FROM states""")
    # Printing states whose name matches the argument
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
