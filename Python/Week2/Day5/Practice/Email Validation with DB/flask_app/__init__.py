from flask import Flask  # type: ignore

app = Flask(__name__)
app.secret_key = 'key23'  # Replace with a secure key in production
DATABASE = "email_schema"  # Database name for your project