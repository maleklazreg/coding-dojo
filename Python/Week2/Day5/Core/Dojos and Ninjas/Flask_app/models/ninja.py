from Flask_app.config.mysqlconnection import MySQLConnection
from Flask_app import DATABASE

class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['name']
        self.last_name = data['last_name']
        self.dojo_id = data['dojo_id']

@classmethod
def save(cls, data):
    query = "INSERT INTO ninjas (name, last_name, dojo_id) VALUES (%(first_name)s, %(last_name)s, %(dojo_id)s);"
    return MySQLConnection(DATABASE).query_db(query, data)