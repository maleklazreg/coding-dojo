from flask_app import app
from flask_app.controllers import email_controller  # Import email controller

if __name__ == "__main__":
    app.run(debug=True)