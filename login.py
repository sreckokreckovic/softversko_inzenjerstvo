# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 21:33:58 2024

@author: Korisnik
"""

import tkinter as tk
import customtkinter as c
from tkinter.messagebox import *
from projekatdb import Database


c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")


class Login(c.CTkFrame):
    def __init__(self, db, master=None):
        super().__init__(master)
        self.db = db
        self.master = master
        self.master.title("Prijava")
        self.master.geometry("1080x720")

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.heading = c.CTkLabel(
            self.master, text="Dobrodosli nazad! Prijavite se na vas nalog...", font=("Verdana", 20,))
        self.heading.pack(pady=30)

        self.frame = c.CTkFrame(self.master)
        self.frame.pack(pady=100)

        for i in range(3):
            self.frame.grid_rowconfigure(i, weight=1)
            self.frame.grid_columnconfigure(0, weight=1, pad=100)
            self.frame.grid_columnconfigure(1, weight=2)

        self.email = self.create_element(self.frame, "Email", 0)
        self.password = self.create_element(
            self.frame, "Password", 1, show="*")
        self.login_b = c.CTkButton(
            self.frame, text='Prijavi se', command=self.login, width=200, font=('Verdana', 15))
        self.login_b.grid(row=2, column=0, columnspan=2, pady=50)

        self.button_frame = c.CTkFrame(self.master)
        self.button_frame.pack()

        self.show_books = c.CTkButton(
            self.button_frame, width=220, text="Pregledaj knjige bez registracije", font=('Verdana', 15))
        self.show_books.pack(side=tk.LEFT, padx=10, pady=10)
        self.show_books = c.CTkButton(
            self.button_frame, width=220, text="Nemate nalog? Registrujte se", font=('Verdana', 15), command=self.open_registration)
        self.show_books.pack(side=tk.LEFT, padx=10, pady=10)

    def create_element(self, frame, text, row, show=None):
        label = c.CTkLabel(frame, text=text, font=('Verdana', 18))
        label.grid(row=row, column=0, padx=10, pady=30, sticky='we')
        entry = c.CTkEntry(frame, width=300, show=show)
        entry.grid(row=row, column=1, padx=(10, 50), pady=30, sticky='w')
        return entry

    def open_registration(self):
        from registration import Registration
        db = Database("library_software.db")
        app = Registration(db)
        app.mainloop()
        self.destroy()

    def login(self):
        email = self.email.get()
        password = self.password.get()
        user = self.db.login_user(email, password)

        if not email or not password:
            tk.messagebox.showerror(
                title='Greška', message='Morate popuniti sva polja')
            return

        try:
            user = self.db.login_user(email, password)
            if user is not None:
                tk.messagebox.showinfo(
                    title='Obavještenje', message='Uspješno ste se prijavili')
            else:
                print(user)
                tk.messagebox.showerror(
                    title='Greška', message='Pogrešno korisničko ime ili lozinka')

        except Exception as e:
            print("Greška prilikom prijave:", e)
            tk.messagebox.showerror(
                title='Greška', message='Pogrešno korisničko ime ili lozinka')


if __name__ == "__main__":
    db = Database("library_software.db")
    root = c.CTk()
    login_page = Login(db, root)
    root.mainloop()
