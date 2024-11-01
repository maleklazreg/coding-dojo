from flask import Flask, render_template,request,session,redirect
from mysqlconnection import connectToMySQL
from users_model import User

app = Flask(__name__)
app.secret_key="password123"


app = Flask(__name__)

@app.route('/user')
def users():
    mysql = connectToMySQL('users_schema') 
    query = "SELECT * FROM users"
    users = mysql.query_db(query) 
    return render_template('users.html', users=users)

@app.route("/user/form",methods=["GET"])
def display_user_form():
    return render_template("create.html")
@app.route("/user/new",methods=["POST"])
def create_user():
    new_user={
        "first_name":request.form["first_name"],
        "last_name":request.form["last_name"],
        "email":request.form["email"]
    }
    result=User.create_one(new_user)
    # list_of_todos.append(new_todo)
    return redirect("/user")

if __name__ == '__main__':
    app.run(debug=True)