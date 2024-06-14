# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:28:27 2024

@author: Korisnik
"""
import customtkinter as c
from login import Login
from projekatdb import Database
from registration import Registration


class Pocetni(c.CTk):
    def __init__(self):
        super().__init__()
        self.title("Softver za biblioteku")
        self.geometry("1080x720")

        self.frame_title = c.CTkFrame(self)
        self.frame_title.grid(row=0, column=0, pady=(50, 0))

        self.label_title = c.CTkLabel(
            self.frame_title, text='DOBRODOŠLI U NAŠU BIBLIOTEKU', font=('Verdana', 30))
        self.label_title.grid(row=0, column=0)

        self.frame_buttons = c.CTkFrame(self)
        self.frame_buttons.grid(row=1, column=0, padx=250, pady=150)

        self.register_btn = c.CTkButton(self.frame_buttons, text='Registracija', width=200, height=50, font=(
            'Verdana', 20), command=self.open_registration)
        self.register_btn.grid(row=0, column=0, padx=50, pady=50)

        self.login_btn = c.CTkButton(self.frame_buttons, text='Prijava', width=200, height=50, font=(
            'Verdana', 20), command=self.open_login)
        self.login_btn.grid(row=0, column=1, padx=50, pady=50)

        self.show_btn = c.CTkButton(self.frame_buttons, text='Pogledaj knjige',
                                    width=200, height=50, font=('Verdana', 20), command=self.open_books)
        self.show_btn.grid(row=1, column=0, padx=50, pady=50)

        self.info_btn = c.CTkButton(self.frame_buttons, text='O nama', width=200, height=50, font=(
            'Verdana', 20), command=self.open_info)
        self.info_btn.grid(row=1, column=1, padx=50, pady=50)

    def open_login(self):
        login_window = c.CTk()
        db = Database("library_software.db")
        Login(db, login_window)
        self.destroy()
        login_window.mainloop()

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

    def open_info(self):
        pass


if __name__ == "__main__":
    app = Pocetni()
    app.mainloop()
