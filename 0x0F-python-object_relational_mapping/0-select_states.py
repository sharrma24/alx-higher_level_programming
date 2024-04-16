#!/usr/bin/python3
import sys
import MySQLdb

def list_states(username, password, database):
    """
    This function lists all states from the 'hbtn_0e_0_usa' database.

    Args:
        username: MySQL username
        password: MySQL password
        database: MySQL database name
    """
    # Establish a connection to the MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    # Execute an SQL query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Print the results
    for row in rows:
        print(row)

    # Close the database connection
    db.close()

# Example usage
if __name__ == '__main__':
    # Extract MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the list_states function with provided arguments
    list_states(username, password, database)

