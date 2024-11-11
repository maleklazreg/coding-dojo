from flask import render_template, redirect, request, session, flash  # Importing necessary modules from Flask for handling HTTP requests, rendering templates, managing sessions, and flashing messages.
from flask_app import app  # Importing the Flask app instance from the main application package.
from flask_app.models.user import User  # Importing the User model to interact with user-related database functionality.
from flask_bcrypt import Bcrypt  # Importing Bcrypt for password hashing.

bcrypt = Bcrypt(app)  # Initializing Bcrypt with the Flask app to use its password-hashing capabilities.

@app.route('/')  # Defining the route for the home page.
def index():
    return render_template('login_register.html')  # Rendering the login and registration page.

@app.route('/register', methods=['POST'])  # Defining the route for handling user registration via POST requests.
def register():
    if not User.validation_user(request.form):  # Validating user input using a method from the User model.
        paw = bcrypt.generate_password_hash(request.form['password'])  # Hashing the user's password with Bcrypt.
        data = {
            **request.form,  # Copying all form data into the new dictionary.
            "password": paw  # Replacing the plain password with the hashed password.
        }
        user_id = User.save(data)  # Saving the new user to the database and retrieving the user's ID.
        session['user_id'] = user_id  # Storing the user's ID in the session to log them in.
        return redirect('/recipes')  # Redirecting the user to the recipes page after registration.
    return redirect('/')  # Redirecting back to the home page if validation fails.

@app.route("/login",methods=["POST"])
def login():
    user=User.get_by_email({'email':request.form["email"]})
    if not user: 
        flash("invalid email/password","login_email")
        return redirect('/') 
    if not bcrypt.check_password_hash(user.password,request.form['password']):
        flash("invalid email/password","login_password")
        return redirect('/') 
    session["user_id"]=user.id 
    return redirect('/after_log')  # Redirecting the user to the recipes page after login.

@app.route('/logout')  # Defining the route for logging out.
def logout():
    session.clear()  # Clearing the session to log the user out.
    return redirect('/')  # Redirecting back to the home page.
