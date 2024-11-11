from flask import render_template, redirect, request, session, flash # type: ignore
from flask_app import app
from flask_app.models.user_model import User
from flask_app.models.friend_model import Friend
from flask_bcrypt import Bcrypt # type: ignore

bcrypt = Bcrypt(app)

@app.route('/')
def regist():
    if 'user_id' not in session:
        return redirect('/')
    friendss = Friend.get_all()
    userss = User.get_by_id({'id':session['user_id']})
    return render_template('index.html', friendss=friendss, userss=userss)

@app.route('/register/create', methods=['POST'])
def create_new():
    if not User.validate_user(request.form):
        pw=bcrypt.generate_password_hash(request.form['password'])
        data = {
            **request.form,
            'password': pw
        }
        user_id=User.save(data)
        session['user_id']=user_id
        return redirect('/dash')
    else:
        return redirect('/')

@app.route('/login', methods=['POST'])
def login():
    user=User.get_one({'email':request.form['email']})
    if not user:
        flash("invalide email/passwor",'login_email')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash("invalid email/password",'login_password')
        return redirect('/')
    session['user_id']=user.id
    return redirect('/dash')

@app.route('/dach')
def home():
    if 'user_id' not in session:
        messages=Friend.message({'id':session['user_id']})
        return render_template('home.html',messages=messages,liste=User.get_all({'id':session["user_id"]}),login_user=User.get_one_by_id({'id':session["user_id"]}),)
    return redirect('/')

@app.route("/logout", methods=['post'])
def logout():
    session.clear()
    return redirect('/')

@app.route('/send/<int:id>', methods=['POST'])
def send(id):
    data={
        'user_id':session['user_id'],
        'friend_id':id,
        "message":request.form['message']
    }
    Friend.get_new_friend(data)
    return redirect('/dach')

@app.route('/remove/message/<int:friend_id>/<int:user_id>', methods=['POST'])
def delete(friend_id,user_id):
    Friend.delete_message({'id':friend_id,'user_id':user_id})
    return redirect('/dash')