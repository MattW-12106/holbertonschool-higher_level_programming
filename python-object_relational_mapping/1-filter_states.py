#!/usr/bin/python3
"""lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa"""

# imports
import MySQLdb
import sys

if __name__ == "__main__":
    """connects to the database and retrieves states with names starting with N"""

    # connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    # create a cursor object
    cursor = db.cursor()

    # execute the SQL query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # fetch all results
    states = cursor.fetchall()

    # print the results
    for state in states:
        print(state)

    # close the database connection
    db.close()