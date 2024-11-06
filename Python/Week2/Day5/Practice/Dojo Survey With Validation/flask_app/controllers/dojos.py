from flask_app import app
from flask import render_template, redirect, request, flash # type: ignore
from flask_app.models.dojos_models import Dojos

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_dojo', methods=['POST'])
def create_dojo():
    errors = Dojos.validate_dojo(request.form)

    if errors:
        for error in errors:
            flash(error, "error")  # Display each error message on the form page
        return redirect('/')  # Redirect back to form if there are errors
    # errors = []
    # if not request.form['name']:
    #     errors.append("Name is required.")
    # elif len(request.form['name']) < 3:
    #     errors.append("Name must be at least 3 characters.")

    # if request.form['location'] == "":
    #     errors.append("Please select a location.")

    # if request.form['language'] == "":
    #     errors.append("Please select a language.")

    # if not request.form['comment']:
    #     errors.append("Comment is required.")
    # elif len(request.form['comment']) < 3:
    #     errors.append("Comment must be at least 3 characters.")
    # if errors:
    #     for error in errors:
    #         flash(error)
    #     return redirect('/')
    # if '_flashes' in request.__dict__:
    #     return redirect('/')

    dojo_id = Dojos.save(request.form)
    return redirect(f'/result/{dojo_id}')

@app.route('/result/<int:id>')
def result(id):
    dojo = Dojos.get_one({'id': id})
    return render_template('result.html', dojo=dojo)
