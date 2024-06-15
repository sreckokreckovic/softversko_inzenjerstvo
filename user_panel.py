# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 18:40:20 2024

@author: Korisnik
"""

import customtkinter as c
from login import Login
from projekatdb import Database
from registration import Registration


class KorisnickiPanel(c.CTk):
    def __init__(self):
        super().__init__()
        self.title("Softver za biblioteku")
        self.geometry("1080x720")
        self.iconbitmap("books_97178.ico")

        self.frame_title = c.CTkFrame(self)
        self.frame_title.grid(row=0, column=0, pady=(50, 0))

        self.label_title = c.CTkLabel(
            self.frame_title, text='User panel', font=('Verdana', 30))
        self.label_title.grid(row=0, column=0)

        self.frame_buttons = c.CTkFrame(self)
        self.frame_buttons.grid(row=1, column=0, padx=250, pady=150)

        self.register_btn = c.CTkButton(self.frame_buttons, text='Pogledaj knjige', width=200, height=50, font=(
            'Verdana', 20),command = self.open_books)
        self.register_btn.grid(row=0, column=0, padx=50, pady=50)

        self.login_btn = c.CTkButton(self.frame_buttons, text='Iznajmi knjigu', width=200, height=50, font=(
            'Verdana', 20),command = self.rent_book)
        self.login_btn.grid(row=0, column=1, padx=50, pady=50)

        self.show_btn = c.CTkButton(self.frame_buttons, text='Vrati knjigu',
                                    width=200, height=50, font=('Verdana', 20), command = self.return_book)
        self.show_btn.grid(row=1, column=0, padx=50, pady=50)

        self.info_btn = c.CTkButton(self.frame_buttons, text='Pocetna stranica', width=200, height=50, font=(
            'Verdana', 20),command = self.open_main)
        self.info_btn.grid(row=1, column=1, padx=50, pady=50)


    def open_main(self):
       from main import Pocetni
       app = Pocetni()
       self.destroy()
       app.mainloop()

    def open_books(self):
        from show_books import ShowBooks
        app  = ShowBooks()
        self.destroy()
        app.mainloop()

    def rent_book(self):
        from rent_book import RentBook
        db = Database("library_software.db")
        app  = RentBook(db)
        self.destroy()
        app.mainloop()
    
    def return_book(self):
        from return_book import ReturnBook
        db = Database("library_software.db")
        app  =ReturnBook(db)
        self.destroy()
        app.mainloop()


if __name__ == "__main__":
    app = KorisnickiPanel()
    app.mainloop()
