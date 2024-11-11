from mysqlconnection import connectToMySQL

DATABASE = "usercr"

class User:
    def __init__(self,data):
        self.id=data['id']
        self.first_name=data['first_name']
        self.last_name=data['last_name']
        self.email=data['email']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(DATABASE).query_db(query)
        users = []
        for row in results:
            users.append(cls(row))
        return users
    
    @classmethod
    def save(cls, data):
        query = " insert into users (first_name, last_name,email) values (%(first_name)s, %(last_name)s, %(email)s); "
        result = connectToMySQL(DATABASE).query_db(query, data)
        return result
