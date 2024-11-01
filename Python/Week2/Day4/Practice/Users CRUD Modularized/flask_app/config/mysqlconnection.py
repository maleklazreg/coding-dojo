import pymysql.cursors

# MySQLConnection class to create and manage a database connection
class MySQLConnection:
    def __init__(self, db):  # Constructor initializes the database connection
        # Establishing a connection to the database
        # Adjust 'user' and 'password' fields based on your MySQL setup
        connection = pymysql.connect(
            host='localhost',              # Database host
            user='root',                   # Database user
            password='root',               # Database password
            db=db,                         # Database name
            charset='utf8mb4',             # Character set for encoding
            cursorclass=pymysql.cursors.DictCursor,  # Cursor returns data as dictionaries
            autocommit=False               # Disable autocommit to handle transactions manually
        )
        self.connection = connection     # Save connection to an instance variable

    def query_db(self, query: str, data: dict = None):  # Method to execute SQL queries
        with self.connection.cursor() as cursor:  # Create a cursor to execute the query
            try:
                query = cursor.mogrify(query, data)  # Prepare and format query with data
                print("Running Query:", query)  # Print query for debugging purposes
     
                cursor.execute(query)  # Execute the query
                if query.lower().find("insert") >= 0:  # Check if query is an INSERT statement
                    self.connection.commit()  # Commit changes for INSERT
                    return cursor.lastrowid  # Return ID of the last inserted row
                elif query.lower().find("select") >= 0:  # Check if query is a SELECT statement
                    result = cursor.fetchall()  # Fetch all rows as dictionaries
                    return result  # Return query result
                else:
                    self.connection.commit()  # Commit changes for UPDATE or DELETE statements
            except Exception as e:  # Catch any exceptions that occur
                print("Something went wrong", e)  # Print error message
                return False  # Return False to indicate query failure
            finally:
                self.connection.close()  # Close the connection after the query is done

# Helper function to create an instance of MySQLConnection
def connectToMySQL(db):  # Takes database name as argument
    return MySQLConnection(db)  # Returns a MySQLConnection instance for the specified database
