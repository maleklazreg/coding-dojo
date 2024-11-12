from flask import render_template, redirect, request, session, flash # type: ignore
from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt # type: ignore

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('login_register.html')

@app.route('/register', methods=['POST'])
def register():
    if User.validation_user(request.form):
        paw = bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form,
                "password":paw 
            }
        user_id = User.save(data)
        session['user_id'] = user_id
        return redirect('/recipes')
    return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    user = User.get_by_email(request.form)
    if not user or not bcrypt.check_password_hash(user.password, request.form['password']):
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/recipes')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

