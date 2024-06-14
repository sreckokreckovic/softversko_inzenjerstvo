# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:40:20 2024

@author: Korisnik
"""

import customtkinter as c
from login import Login
from projekatdb import Database
from registration import Registration


class Admin(c.CTk):
    def __init__(self):
        super().__init__()
        self.title("Softver za biblioteku")
        self.geometry("1080x720")

        self.frame_title = c.CTkFrame(self)
        self.frame_title.grid(row=0, column=0, pady=(50, 0))

        self.label_title = c.CTkLabel(
            self.frame_title, text='Admin panel', font=('Verdana', 30))
        self.label_title.grid(row=0, column=0)

        self.frame_buttons = c.CTkFrame(self)
        self.frame_buttons.grid(row=1, column=0, padx=250, pady=150)

        self.register_btn = c.CTkButton(self.frame_buttons, text='Dodaj knjigu', width=200, height=50, font=(
            'Verdana', 20),command = self.add_book)
        self.register_btn.grid(row=0, column=0, padx=50, pady=50)

        self.login_btn = c.CTkButton(self.frame_buttons, text='Izbrisi knjigu', width=200, height=50, font=(
            'Verdana', 20),command = self.delete_book)
        self.login_btn.grid(row=0, column=1, padx=50, pady=50)

        self.show_btn = c.CTkButton(self.frame_buttons, text='Dodaj korisnika',
                                    width=200, height=50, font=('Verdana', 20), command = self.open_registration)
        self.show_btn.grid(row=1, column=0, padx=50, pady=50)

        self.info_btn = c.CTkButton(self.frame_buttons, text='Dostupne knjige', width=200, height=50, font=(
            'Verdana', 20),command = self.open_books)
        self.info_btn.grid(row=1, column=1, padx=50, pady=50)


    def open_registration(self):
        db = Database("library_software.db")
        app = Registration(db)
        self.destroy()
        app.mainloop()

    def open_books(self):
       from show_books import ShowBooks
       app  = ShowBooks()
       self.destroy()
       app.mainloop()

    def add_book(self):
        from add_book import AddBook
        db = Database("library_software.db")
        app = AddBook(db)
        self.destroy()
        app.mainloop()
    
    def delete_book(self):
        from delete_book import DeleteBook
        db = Database("library_software.db")
        app = DeleteBook(db)
        self.destroy()
        app.mainloop()


if __name__ == "__main__":
    app = Admin()
    app.mainloop()
