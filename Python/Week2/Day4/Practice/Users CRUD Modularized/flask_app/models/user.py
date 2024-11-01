from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import DATABASE

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

@classmethod
def get_all(cls):
    query = "select * from users;"
    results = connectToMySQL(DATABASE).query_db(query)
    users = []
    for user in results:
        users.append(cls(user))
    return users

@classmethod
def get_one(cls, data):
    query = "select * from users where id = %(id)s;"
    results = connectToMySQL(DATABASE).query_db(query, data)
    return cls(results[0])

@classmethod
def create(cls, data):
    query = "insert into users (first_name, last_name, email,) values(%(first_name)s,%(last_name)s,%(email)s) "
    id = connectToMySQL(DATABASE).query_db(query, data)
    return id

@classmethod
def update(cls, data):
    query = "update users set first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s"
    return connectToMySQL(DATABASE).query_db(query, data)

@classmethod
def delete(cls, data):
    query = "delete from users where id = %(id)s;"
    return connectToMySQL(DATABASE).query_db(query, data)
