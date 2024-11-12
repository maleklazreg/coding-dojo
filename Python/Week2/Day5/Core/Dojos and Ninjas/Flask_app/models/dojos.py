from Flask_app.config.mysqlconnection import MySQLConnection
from Flask_app import DATABASE

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

@classmethod
def get_all(cls):
    query = "SELECT * FROM dojos"
    results = MySQLConnection(DATABASE).query_db(query)
    dojos = []
    for row in results:
        dojos.append(cls(row))
    return dojos

@classmethod
def save(cls, data):
    query = "INSERT INTO dojos (name) VALUES (%(name)s);"
    return MySQLConnection(DATABASE).query_db(query, data)

@classmethod
def get_with_ninjas(cls, dojo_id):
    query = "select * from dojos left join ninjas on dojos.id = ninjas.dojo_id where dojos.id = %(dojo_is)s;"
    data = {'dojo_id': dojo_id}
    results = MySQLConnection(DATABASE).query_db(query, data)
    dojo = cls(results[0])
    dojo.ninjas = []
    for row in results:
        if row['ninjas.id'] is not None:
            ninja_data = {
                'id': row['ninjas.id'],
                'first_name': row['ninjas.first_name'],
                'last_name': row['ninjas.last_name'],
                'dojo_id' : row['dojo_id']
            }
            dojo.ninjas.append(ninja_data)
        return dojo


