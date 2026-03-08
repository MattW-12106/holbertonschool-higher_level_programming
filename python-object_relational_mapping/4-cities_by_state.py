#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

# imports
import MySQLdb
import sys

if __name__ == "__main__":
    # connect to the database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    
    # create a cursor object
    cursor = db.cursor()
    
    # execute the SQL query
    query = "SELECT cities.id, cities.name, states.name \
             FROM cities JOIN states ON cities.state_id = states.id \
             ORDER BY cities.id ASC"
    cursor.execute(query)
    
    # fetch all the results
    results = cursor.fetchall()
    
    # print the results
    for row in results:
        print(row)
    
    # close the database connection
    db.close()