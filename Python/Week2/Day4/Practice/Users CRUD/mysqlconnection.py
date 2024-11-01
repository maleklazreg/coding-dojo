import mysql.connector
from mysql.connector import errorcode

class MySQLConnection:
    def __init__(self, db):
        try:
            self.conn = mysql.connector.connect(
                user='your_username',
                password='your_password',
                host='localhost',
                database=db
            )
            self.cursor = self.conn.cursor(dictionary=True)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
    
    def query_db(self, query, data=None):
        try:
            self.cursor.execute(query, data)
            if query.lower().startswith('select'):
                return self.cursor.fetchall()
            else:
                self.conn.commit()
                return self.cursor.lastrowid
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    app.run(debug=True)