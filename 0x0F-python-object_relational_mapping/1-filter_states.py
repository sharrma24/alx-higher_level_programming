#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Extract MySQL credentials from command-line arguments
    # Establish a connection to the MySQL server
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()

    # Execute an SQL query to retrieve all states sorted by id
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")

    # Print states whose names start with 'N'
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]

    # Close the database connection
    db.close()

