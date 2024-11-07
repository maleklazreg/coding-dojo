from flask import render_template, request, redirect, flash
from flask_app import app
from flask_app.models.email_model import Email

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')  # Render the form page when the method is GET

@app.route("/email", methods=["POST"])
def register():
    # Validate the email and insert it if valid
    if Email.validate_email_format(request.form):
        data = { 
            "email": request.form['email']
        }
        Email.creat(data)  # Create the email record in the database
        return redirect("/submit")  # Redirect to the 'submit' page after successful submission
    else:
        return redirect("/")  # Redirect back to the form page if validation fails

@app.route('/submit')
def submit():
    # Display all emails with timestamps
    return render_template('submit.html', emails=Email.get_all())  # Render the submit page with all emails
