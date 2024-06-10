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
        self.con.commit()
        
    def register_user(self,name,surname,age,contact,email,password,is_admin):
        self.cr.execute("INSERT INTO users (name, surname, age, contact, email, password, is_admin) VALUES (?,?,?,?,?,?,?)", (name, surname, age, contact, email, password, is_admin))
        self.con.commit()
        
    def login_user(self,email,password):
        self.cr.execute("SELECT * FROM users WHERE email = ? AND password = ?", (email, password))
        user = self.cr.fetchone()
        return user
        