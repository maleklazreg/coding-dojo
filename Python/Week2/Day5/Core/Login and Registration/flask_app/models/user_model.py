from flask_app import DATABASE
from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash 
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User: 
    def __init__(self,data): 
        self.id=data["id"]
        self.first_name=data["first_name"]
        self.last_name=data["last_name"]
        self.email=data["email"]
        self.password=data["password"]
        self.created_at=data["created_at"]
        self.updated_at=data["updated_at"]


    @classmethod 
    def register(cls,data): 
        qurey="insert into users(first_name,last_name,email,password) values(%(first_name)s,%(last_name)s,%(email)s,%(password)s);"
        return connectToMySQL(DATABASE).query_db(qurey,data) 
    
    @classmethod
    def get_by_email(cls,data):
        qurey="select * from users where email =%(email)s;"
        result=connectToMySQL(DATABASE).query_db(qurey,data) 
        if result:
            return cls(result[0]) 
        return False 
    @classmethod

    def get_by_id(cls,data):
        qurey="select *from users where id =%(id)s;"
        result=connectToMySQL(DATABASE).query_db(qurey,data) 
        if result:
            return cls(result[0]) 
        return False


    @staticmethod
    def validate(data):
        is_valid = True
        # Check first name length
        if len(data["first_name"]) < 2:
            flash("First name must be at least 2 characters.", "first_name")
            is_valid = False

        # Check last name length
        if len(data["last_name"]) < 2:
            flash("Last name must be at least 2 characters.", "last_name")
            is_valid = False

        # Validate email format and uniqueness
        if not EMAIL_REGEX.match(data["email"]):
            flash("Invalid email format.", "email")
            is_valid = False
        elif User.get_by_email({"email": data['email']}):
            flash("Email already taken.", "email")
            is_valid = False

        # Validate password length and match with confirmation
        if len(data["password"]) < 7:
            flash("Password must contain at least 7 characters.", "password")
            is_valid = False
        elif data["password"] != data["confirm_password"]:
            flash("Passwords do not match.", "confirm_password")
            is_valid = False

        return is_valid