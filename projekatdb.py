# -*- coding: utf-8 -*-
"""
Created on Sun Jun  9 14:02:34 2024

@author: Korisnik
"""

import sqlite3

class Database:
    def __init__(self,database):
        self.con = sqlite3.connect(database)
        self.cr = self.con.cursor()
        users_sql = """
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            age INTEGER,
            contact TEXT,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            is_admin INTEGER
            )
        """
        self.cr.execute(users_sql)
        
        books_sql="""
        CREATE TABLE IF NOT EXISTS books(
            book_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            description TEXT,
            available INTEGER,
            genre TEXT
            )
        
        """
        self.cr.execute(books_sql)
        reservations_sql = """
        CREATE TABLE IF NOT EXISTS reservations(
            reservation_id INTEGER PRIMARY KEY AUTOINCREMENT,
            book_id INT NOT NULL,
            user_id INT NOT NULL
            )
        """
        self.cr.execute(reservations_sql)
        
        comments_sql = """
        CREATE TABLE IF NOT EXISTS comments(
            comment_id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            text TEXT NOT NULL
            )
        """
        self.cr.execute(comments_sql)
        self.con.commit()
        
    def add_comment(self,title,text):
        self.cr.execute("INSERT INTO comments(title,text) VALUES(?,?)",(title,text))
        self.cr.commit()
        
        
    def register_user(self,name,surname,age,contact,email,password,is_admin):
        self.cr.execute("INSERT INTO users (name, surname, age, contact, email, password, is_admin) VALUES (?,?,?,?,?,?,?)", (name, surname, age, contact, email, password, is_admin))
        self.con.commit()
        
    def login_user(self,email,password):
        self.cr.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = self.cr.fetchone()
        return user
    def add_book(self,name,author,year,description,available,genre):
        self.cr.execute("INSERT INTO books (name,author,year,description,available,genre) VALUES (?,?,?,?,?,?)", (name,author,year,description,available,genre))
        self.con.commit()
    def delete_book(self,id):
        self.cr.execute("DELETE FROM books WHERE book_id=?",(id,))
        self.con.commit()
        return 1
    def add_reservation(self,book_id,email):
        self.cr.execute("SELECT user_id FROM users WHERE email=?", (email,))
        user_id = self.cr.fetchone()
        if user_id is not None:
            user_id = user_id[0]
            self.cr.execute("INSERT INTO reservations(book_id,user_id) VALUES(?,?)",(book_id,user_id))
            self.cr.execute("UPDATE books SET available=? WHERE book_id=?",(0,book_id))
            self.con.commit()
    def return_book(self,book_id,email):
        self.cr.execute("SELECT user_id FROM users WHERE email=?", (email,))
        user_id = self.cr.fetchone()
        if user_id is not None:
            user_id = user_id[0]
            self.cr.execute("DELETE FROM reservations WHERE book_id=? AND user_id=?",(book_id,user_id))
            self.cr.execute("UPDATE books SET available=? WHERE book_id=?",(1,book_id))
            self.con.commit()
    def available_books(self):
        self.cr.execute("SELECT * FROM books WHERE available=?",(1,))
        available_books = self.cr.fetchall()
        return available_books
    def get_book_by_id(self, book_id):
        self.cr.execute("SELECT * FROM BOOKS WHERE book_id = ?", (book_id,))
        return self.cr.fetchone()
        
        