from flask_app.config.mysqlconnection import connectToMySQL  # Import the database connection function
from flask import flash  # type: ignore # Import flash for displaying messages
from flask_app import DATABASE  # Import the database
import re  # Import regular expressions for email validation
from flask_bcrypt import Bcrypt  # type: ignore # Import Bcrypt for password hashing
from flask_app import app  # Import the Flask application instance

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')  # Define a regex pattern for email validation

bcrypt = Bcrypt(app)  # Initialize Bcrypt with the app for password hashing

class User:
    def __init__(self, data):  # Initialize the User class with user data
        self.id = data['id']  # Set the user's ID
        self.first_name = data['first_name']  # Set the user's first name
        self.last_name = data['last_name']  # Set the user's last name
        self.email = data['email']  # Set the user's email
        self.password = data['password']  # Set the user's password
        self.created_at = data['created_at']  # Set the account creation timestamp
        self.updated_at = data['updated_at']  # Set the account last updated timestamp
    
    @classmethod
    def save(cls, data):  # Save a new user to the database
        query = """insert into users (first_name, last_name, email, password)
        values (%(first_name)s,%(last_name)s,%(email)s,%(password)s);"""
        return connectToMySQL(DATABASE).query_db(query, data)  # Execute the query with provided data
    
    @classmethod
    def get_by_email(cls, data):  # Retrieve a user by their email
        query = "select * from users where email = %(email)s;"  # SQL query to find a user by email
        result = connectToMySQL(DATABASE).query_db(query, data)  # Execute the query
        if result:  # Check if a result is found
            return cls(result[0])  # Return the User object if found
        return False  # Return False if no user found
    
    @classmethod
    def get_user_by_id(cls, data):  # Retrieve a user by their ID
        query = "select * from users where id = %(id)s;"  # SQL query to find a user by ID
        result = connectToMySQL(DATABASE).query_db(query, data)  # Execute the query
        if result:  # Check if a result is found
            return cls(result[0])  # Return the User object if found
        return False  # Return False if no user found
    
    @staticmethod
    def validation_user(data):  # Validate user data before saving to database
        is_valid = True  # Initialize validation status as True
        # First name validation
        if len(data.get('first_name')) < 2:  # Check if first name is at least 2 characters
            flash("First name must be at least 2 characters.", "first_name")  # Flash an error message
            is_valid = False  # Set validation status to False
        # Last name validation
        if len(data.get('last_name')) < 2:  # Check if last name is at least 2 characters
            flash("Last name must be at least 2 characters.", "last_name")  # Flash an error message
            is_valid = False  # Set validation status to False
        # Email validation
        if not EMAIL_REGEX.match(data.get('email')):  # Check if email format is valid
            flash("Invalid email format.", "email")  # Flash an error message
            is_valid = False  # Set validation status to False
        elif User.get_by_email({'email': data.get('email')}):  # Check if email is already registered
            flash("Email already registered. Please log in.", "email1")  # Flash an error message
            is_valid = False  # Set validation status to False
        # Password validation
        if len(data.get('password')) < 8:  # Check if password is at least 8 characters
            flash("Password must be at least 8 characters.", "password")  # Flash an error message
            is_valid = False  # Set validation status to False
        elif data.get('password') != data.get('confirm_password'):  # Check if passwords match
            flash("Passwords do not match.", "confirm_password")  # Flash an error message
            is_valid = False  # Set validation status to False
        return is_valid  # Return the validation status
