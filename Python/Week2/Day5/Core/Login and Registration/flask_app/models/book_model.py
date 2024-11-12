from flask_app.config.mysqlconnection import MySQLConnection
from flask import flash
from flask_app import DATABASE

class Book:
    def __init__(self,data):
        self.id = data['id']
        self.title = data['title']
        self.author = data['author']
        self.thoughts = data['thoughts']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.posted_by = ""

    @classmethod
    def create(cls, data):
        query = """ insert into books (title, author, thoughts, user_id) 
                    values (%(title)s,%(author)s,%(thoughts)s,%(user_id)s); """
        return MySQLConnection(DATABASE).query_db(query,data)


    @classmethod
    def get_all(cls):
        query = """ select * from books join users on books.user_id = users.id; """
        results = MySQLConnection(DATABASE).query_db(query)
        books = []
        for row in results:
            book = cls(row)
            book.posted_by = f"{row['first_name']} {row['last_name']}"
            books.append(book)
        return books
    
    @classmethod
    def get_by_id(cls, data):
        query = """ select * from books join users on 
        books.user_id = users.id where books.id= %(id)s; """
        results = MySQLConnection(DATABASE).query_db(query, data)
        book = cls(results[0])
        book.posted_by = f"{results[0]['first_name']} {results[0]['last_name']}"
        return book

    @classmethod
    def update(cls, data):
        query = """ update books set title = %(title)s,author = %(author)s,thoughts = %(thoughts)s
         where id= %(id)s """
        return MySQLConnection(DATABASE).query_db(query, data)
    
    @classmethod
    def delete(cls, data):
        query = """ delete from books where id = %(id)s """
        return MySQLConnection(DATABASE).query_db(query, data)
    
    @staticmethod
    def validate(data):
        is_valid = True
        if len(data['title']) < 2:
            flash("Tile must contain at least 2 caracters", "title")
            is_valid = False
        if len(data['author']) < 2:
            flash("Author must contain at least 2 caracters", "author")
            is_valid = False
        if len(data['thoughts']) < 7:
            flash("Thoughts must contain at least 7 caracters", "thoughts")
            is_valid = False
        return is_valid
