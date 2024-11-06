from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Dojos:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojo;"
        results = connectToMySQL(DATABASE).query_db(query)
        all_dojos = [cls(row) for row in results]
        return all_dojos

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojo WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        return cls(result[0]) if result else None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojo (name, location, language, comment) VALUES (%(name)s, %(location)s, %(language)s, %(comment)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    @staticmethod
    def validate_dojo(data):
        errors = []
        # Check if name is at least 3 characters and not empty
        if len(data['name'].strip()) < 3:
            errors.append("Name must be at least 3 characters.")

        # Check if comment is at least 3 characters and not empty
        if len(data['comment'].strip()) < 3:
            errors.append("Comment must be at least 3 characters.")

        # Check if location is selected
        if data['location'] == "":  # Adjust depending on how empty values are stored
            errors.append("Location must be selected.")

        # Check if language is selected
        if data['language'] == "":  # Adjust depending on how empty values are stored
            errors.append("Language must be selected.")

        return errors  # Returns list of error messages

    # @classmethod
    # def update(clas,data) :
    #     query="UPDATE users SET name=%(name)s,location=%(location)s,language=%(language)s,comment=%(comment)s WHERE  dojo.id=%(id)s ; "
    #     return connectToMySQL(DATABASE).query_db(query,data)


    # @classmethod
    # def delete(clas,data) :
    #     query="DELETE FROM dojo WHERE id=%(id)s ;"
    #     return  connectToMySQL(DATABASE).query_db(query,data)