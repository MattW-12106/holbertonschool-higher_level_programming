#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa"""

# imports
import MySQLdb
import sys

# main function
if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # connect to the database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
        )
    
    # create a cursor object
    cursor = db.cursor()

    # execute the SQL query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # fetch all the results
    states = cursor.fetchall()

    # print the results
    for state in states:
        print(state)
    
    # close the cursor and the database connection
    cursor.close()
    db.close()