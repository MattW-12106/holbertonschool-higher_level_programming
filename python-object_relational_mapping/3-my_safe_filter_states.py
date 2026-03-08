#!/usr/bin/python3
"""
takes in arguments and displays all values in the states table of 
hbtn_0e_0_usa where name matches the argument. 
But this time, write one that is safe from MySQL injections!
"""

# imports
import MySQLdb
import sys

if __name__ == "__main__":
    # connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    
    # create a cursor object
    cursor = db.cursor()
    
    # execute the query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))
    
    # fetch all the results
    results = cursor.fetchall()
    
    # print the results
    for row in results:
        print(row)

    # close the cursor and the connection
    cursor.close()
    db.close()
