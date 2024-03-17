#!/usr/bin/python3
"""This script takes in an argument and displays all values
   in the states table of hbtn_0e_0_usa where the name matches the argument.
   Usage: ./2-my_filter_states.py <mysql username>
                                 <mysql password>
                                 <database name>
                                 <state name searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Establishing a connection to the MySQL database
    db = MySQLdb.connect(user=sys.argv[1],
				passwd=sys.argv[2], db=sys.argv[3])
    # Creating a cursor object
    c = db.cursor()
    # Executing the SQL query to select states where the name
    matches the argument
    c.execute("""SELECT * FROM states
                WHERE name LIKE BINARY '{}'
                ORDER BY states.id ASC""".format(sys.argv[4]).strip("'"))
    # Printing the fetched states
    [print(state) for state in c.fetchall()]
