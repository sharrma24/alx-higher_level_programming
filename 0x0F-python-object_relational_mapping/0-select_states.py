#!/usr/bin/python3
import sys
import MySQLdb

def list_states(username, password, database_name):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        user=username,
        passwd=password,
        db=database_name,
        port=3306
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute SQL query to fetch states sorted by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

# Check if script is being executed directly
if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script_name.py mysql_username mysql_password database_name")
        sys.exit(1)

    # Extract arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Call the function to list states
    list_states(mysql_username, mysql_password, database_name)

