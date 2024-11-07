from flask_app.config.mysqlconnection import connectToMySQL 
from flask import flash
import re
from datetime import datetime

# Regular expression to validate email format
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_email(cls, data):
        # Check if the email already exists in the database
        query = "SELECT * FROM emails WHERE email = %(email)s;"
        result = connectToMySQL('email_schema').query_db(query, data)
        return len(result) > 0  # If result is not empty, email exists

    @classmethod
    def get_all(cls):
        # Get all emails in the database ordered by creation date
        query = "SELECT * FROM emails ORDER BY created_at DESC;"
        result = connectToMySQL('email_schema').query_db(query)
        return [cls(row) for row in result]  # Return instances of the Email class

    @classmethod
    def creat(cls, data):
        # Insert a new email record into the database
        query = "INSERT INTO emails (email, created_at) VALUES (%(email)s, NOW());"
        return connectToMySQL('email_schema').query_db(query, data)

    @staticmethod 
    def validate_email_format(data): 
        # Validate email format using regex
        is_valid = True
        email = data.get("email")

        if not EMAIL_REGEX.match(email):
            flash("Email is not valid!", 'error')
            is_valid = False
        
        # Check if the email already exists
        elif Email.get_email({"email": email}):
            flash("This email is already written!", 'error')
            is_valid = False

        if is_valid:
            flash("Email successfully added!", 'success')
        
        return is_valid  # Return True if valid, False otherwise