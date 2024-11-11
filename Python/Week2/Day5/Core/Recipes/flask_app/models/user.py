from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash # type: ignore
from flask_app import DATABASE # type: ignore
import re
from flask_bcrypt import Bcrypt # type: ignore
from flask_app import app

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

bcrypt = Bcrypt(app)

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def save(cls, data):
        query = """insert into users (first_name, last_name, email, password)
        values (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"""
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_by_email(cls,data):
        query = "select * from users where email = %(email)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return False
    
    @classmethod
    def get_user_by_id(cls,data):
        query = "select * from users where id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            return cls(result[0])
        return False
    
    @staticmethod
    def validation_user(data):
        is_valid = True
        # First name validation
        if len(data.get('first_name')) < 2:
            flash("First name must be at least 2 characters.", "first_name")
            is_valid = False
        # Last name validation
        if len(data.get('last_name')) < 2:
            flash("Last name must be at least 2 characters.", "last_name")
            is_valid = False
        # Email validation
        if not EMAIL_REGEX.match(data.get('email')):
            flash("Invalid email format.", "email")
            is_valid = False
        elif User.get_by_email({'email': data.get('email')}):
            flash("Email already registered. Please log in.", "email1")
            is_valid = False
        # Password validation
        if len(data.get('password')) < 8:
            flash("Password must be at least 8 characters.", "password")
            is_valid = False
        elif data.get('password') != data.get('confirm_password'):
            flash("Passwords do not match.", "confirm_password")
            is_valid = False
        return is_valid
    


    