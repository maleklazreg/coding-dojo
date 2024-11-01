from flask import Flask, render_template, redirect, request, flash, url_for
from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = 'your_secret_key'
mysql = MySQLConnection('your_database_name')

@app.route('/users')
def users():
    query = "SELECT id, CONCAT(first_name, ' ', last_name) AS full_name, email, created_at FROM users;"
    users = mysql.query_db(query)
    return render_template('users.html', users=users)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')

@app.route('/users/create', methods=['POST'])
def create_user():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (%s, %s, %s, NOW(), NOW());"
    data = (first_name, last_name, email)
    mysql.query_db(query, data)
    return redirect('/users')

@app.route('/users/<int:user_id>')
def user_detail(user_id):
    query = "SELECT * FROM users WHERE id = %s;"
    user = mysql.query_db(query, (user_id,))
    return render_template('user.html', user=user[0])

@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    query = "SELECT * FROM users WHERE id = %s;"
    user = mysql.query_db(query, (user_id,))
    return render_template('edit_user.html', user=user[0])

@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    query = "UPDATE users SET first_name = %s, last_name = %s, email = %s, updated_at = NOW() WHERE id = %s;"
    data = (first_name, last_name, email, user_id)
    mysql.query_db(query, data)
    return redirect(f'/users/{user_id}')

@app.route('/users/<int:user_id>/delete')
def delete_user(user_id):
    query = "DELETE FROM users WHERE id = %s;"
    mysql.query_db(query, (user_id,))
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)
