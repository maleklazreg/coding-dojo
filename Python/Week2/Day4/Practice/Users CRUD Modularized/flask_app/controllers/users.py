from flask_app import app
from flask import render_template, redirect, request  # type: ignore
from flask_app.models.user import User

@app.route('/users')
def index():
    all_users = User.get_all()
    return render_template('index.html', all_users=all_users)

@app.route('/users/new')
def new():
    return render_template('new.html')

@app.route('/users/create', methods=['POST'])
def create():
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }
    User.create(data)
    return redirect('/users')

@app.route('/users/<int:user_id>/')
def show(user_id):
    data = {
        "id": user_id
    }
    user = User.get_one(data)
    return render_template('user.html', user=user)

@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete(user_id):
    data = {
        "id": user_id
    }
    User.delete(data)
    return redirect('/users')

@app.route('/users/<int:id>/update')
def update_post(id):
    user = User.get_one({'id': id})
    return render_template('update.html', user=user)

@app.route('/users/update_user', methods=['POST'])
def submit_update():
    User.update(request.form)
    return redirect('/users')
