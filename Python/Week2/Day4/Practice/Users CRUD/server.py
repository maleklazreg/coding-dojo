from flask import Flask, render_template, redirect, request, url_for  # type: ignore
from mysqlconnection import MySQLConnection

app = Flask(__name__)
app.secret_key = 'your_secret_key'
DATABASE = 'crud_schema'


@app.route('/users')
def users():
    query = "select * from users"
    users = MySQLConnection(DATABASE).query_db(query)
    return render_template('users.html', users=users)

@app.route('/users/new')
def new_user():
    return render_template('new_user.html')
    

@app.route('/users/creat', methods=['POST'])
def create_user():
    query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    new_user_id = MySQLConnection(DATABASE).query_db(query, data)
    return redirect(url_for('user', user_id=new_user_id))

@app.route('/users/<int:user_id>')
def user(user_id):
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {'id': user_id}
    user = MySQLConnection(DATABASE).query_db(query, data)[0]
    return render_template('user.html', user=user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {'id': user_id}
    user = MySQLConnection(DATABASE).query_db(query, data)[0]
    return render_template('edit_user.html', user=user)


@app.route('/users/<int:user_id>/update', methods=['POST'])
def update_user(user_id):
    query = "update users SET first_name = %(first_name)s, last_name = %(last_name)s, email = %(email)s, updated_at = now()where id = %(id)s;"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'id': user_id
    }
    MySQLConnection(DATABASE).query_db(query, data)
    return redirect(url_for('user', user_id=user_id))

# i can't do this i try all the thinks i got but he didint work 
@app.route('/users/<int:user_id>/delete', methods=['POST'])
def delete_user(user_id):
    query = "DELETE FROM users WHERE id = %(id)s;"
    data = {'id': user_id}
    MySQLConnection(DATABASE).query_db(query, data)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)