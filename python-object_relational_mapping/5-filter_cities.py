#!/usr/bin/python3
"""
takes in the name of a state as an argument and 
lists all cities of that state, using the database hbtn_0e_4_usa
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
    
    # execute the query to get cities of the state
    query = """SELECT cities.name FROM cities
               JOIN states ON cities.state_id = states.id
               WHERE states.name = %s ORDER BY cities.id ASC"""
    cursor.execute(query, (sys.argv[4],))
    
    # fetch all results
    results = cursor.fetchall()
    
    # print the city names separated by commas
    city_names = [row[0] for row in results]
    print(", ".join(city_names))
    
    # close the database connection
    db.close()