from flask_app import app
from flask import render_template, redirect, session, request # type: ignore
from flask_app.models.book_model import Book
from flask_app.models.user_model import User

@app.route('/books/new')
def new_book():
    if not 'user_id' in session:
        return redirect('/')
    return render_template('new_book.html')

@app.route('/books/create', methods=['post'] )
def add_book():
    if Book.validate(request.form):
        data = {
            **request.form,
            "user_id":session['user_id']
        }
        Book.create(data)
        return redirect('/dashbord')
    return redirect('/books/new')

@app.route('/dashbord')
def dashboard():
    if not 'user_id' in session:
        return redirect('/')
    user = User.get_by_id({'id': session['user_id']})
    all_books = Book.get_all()
    return render_template('dashbord.html', user=user , all_books=all_books)

@app.route('/books/<int:book_id>')
def show_book(book_id):
    if not 'user_id' in session:
        return redirect('/')
    book = Book.get_by_id({'id': book_id})
    return render_template('show.html', book=book)

@app.route('/books/edit/<int:book_id>')
def edit(book_id):
    if not 'user_id' in session:
        return redirect('/')
    book = Book.get_by_id({'id': book_id})
    return render_template('edit.html', book=book)

@app.route('/books/delete/<int:book_id>', methods=['post'] )
def delete(book_id):
    Book.delete({'id': book_id})
    return redirect('/dashbord')
    

@app.route('/books/update/<int:book_id>', methods=['post'])
def update(book_id):
    if Book.validate(request.form):
        data = {
            **request.form,
            "id": book_id
        }
        Book.update(data)
        return redirect('/dashbord')
    return redirect(f'/books/edit/{book_id}')