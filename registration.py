# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 17:37:42 2024

@author: Korisnik
"""

import tkinter as tk
import customtkinter as c
from tkinter.messagebox import *
from projekatdb import Database
from login import Login

c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")


class Registration(c.CTk):
    def __init__(self, db, master=None):
        super().__init__(master)
        self.db = db
        self.master = master

        self.title("Softver za biblioteku")
        self.geometry("1080x720")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_label = c.CTkLabel(
            self, text="Registrujte se", font=("Verdana", 40))
        self.title_label.grid(row=0, column=0, columnspan=2)

        self.frame = c.CTkFrame(self)
        self.frame.grid(row=1, column=0, padx=10, pady=80, sticky='n')

        for i in range(7):
            self.frame.grid_rowconfigure(i, weight=1)
            self.frame.grid_columnconfigure(0, weight=1, pad=100)
            self.frame.grid_columnconfigure(1, weight=2)
        self.name = self.create_elements(self.frame, "Ime", 0)
        self.surname = self.create_elements(self.frame, "Prezime", 1)
        self.age = self.create_elements(self.frame, "Godine", 2)
        self.contact = self.create_elements(self.frame, "Kontakt", 3)
        self.email = self.create_elements(self.frame, "Email", 4)
        self.password = self.create_elements(
            self.frame, "Sifra", 5, show='*')
        self.register_b = c.CTkButton(
            self.frame, text='Registruj se', command=self.register, width=200, font=('Verdana', 15))
        self.register_b.grid(row=6, column=0, columnspan=2, pady=10)

        self.button_frame = c.CTkFrame(self)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=30)
        self.login_b = c.CTkButton(self.button_frame, text="Imate već nalog? Prijavite se", font=(
            'Verdana', 15), width=200, command=self.open_login_window)
        self.login_b.grid(row=0, column=0, padx=10)
        
        self.show_main = c.CTkButton(
            self.button_frame, text="Pocetna", font=('Verdana', 15), width=220,command = self.open_main)
        self.show_main.grid(row=0, column=2, padx=10)
        

    def register(self):
        name = self.name.get()
        surname = self.surname.get()
        age = self.age.get()
        contact = self.contact.get()
        email = self.email.get()
        password = self.password.get()

        if not name and not surname and not email and not age and not password:
            tk.messagebox.showerror(
                title='Greska', message='Morate popuniti sva polja')
            return

        try:
            self.db.register_user(name, surname, age,
                                  contact, email, password, is_admin=0)
            tk.messagebox.showinfo(title='Obavjestenje',
                                   message='Uspjesno registrovan korisnik')
            self.clear_all()
        except Exception as e:
            tk.messagebox.showerror(
                title='Greska', message='Vec postoji korisnik sa istom email adresom')

    def clear_all(self):
        self.name.delete(0, 'end')
        self.surname.delete(0, 'end')
        self.age.delete(0, 'end')
        self.contact.delete(0, 'end')
        self.email.delete(0, 'end')
        self.password.delete(0, 'end')

    def create_elements(self, frame, text, row, show=None):
        label = c.CTkLabel(frame, text=text)
        label.grid(row=row, column=0, padx=15, pady=15, sticky='we')
        entry = c.CTkEntry(frame, width=300, show=show)
        entry.grid(row=row, column=1, padx=15, pady=15, sticky='w')
        return entry

    def open_login_window(self):
        login_window = c.CTk()
        Login(self.db, login_window)
        self.destroy()
        login_window.mainloop()

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
    
        

if __name__ == "__main__":
    db = Database("library_software.db")
    app = Registration(db)
    app.mainloop()
