# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 00:34:29 2024

@author: Korisnik
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 00:21:30 2024

@author: Korisnik
"""

import tkinter as tk
import customtkinter as c  

from tkinter import messagebox  
from projekatdb import Database


c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")


class ReturnBook(c.CTk):
    def __init__(self, db, master=None):
        super().__init__(master)
        self.db = db
        self.master = master

        self.title("Softver za biblioteku")
        self.geometry("1080x720")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_label = c.CTkLabel(
            self, text="Vrati knjigu", font=("Verdana", 20))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=30)

        self.frame = c.CTkFrame(self)
        self.frame.grid(row=1, column=0, padx=0, pady=120, sticky='n')

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1, pad=20)
        self.frame.grid_columnconfigure(1, weight=2)
        
        self.user_id_label = c.CTkLabel(self.frame, text="ID korisnika")
        self.user_id_label.grid(row=0, column=0, padx=15, pady=15, sticky='we')

        self.user_id_entry = c.CTkEntry(self.frame, width=300)
        self.user_id_entry.grid(row=0, column=1, padx=15, pady=15, sticky='w')

        self.book_id_label = c.CTkLabel(self.frame, text="ID knjige")
        self.book_id_label.grid(row=1, column=0, padx=15, pady=15, sticky='we')

        self.book_id_entry = c.CTkEntry(self.frame, width=300)
        self.book_id_entry.grid(row=1, column=1, padx=15, pady=15, sticky='w')

        self.delete_book_b = c.CTkButton(
            self.frame, text='Vrati  knjigu', command=self.return_book, width=200, font=('Verdana', 15))
        self.delete_book_b.grid(row=2, column=0, columnspan=2, pady=10)

        
        self.create_menu()

    def return_book(self):
        book_id = self.book_id_entry.get()
        user_id = self.user_id_entry.get()

        if not book_id and not user_id:
            tk.messagebox.showerror(
                title='Greška', message='Morate popuniti sva polja')
            return

        try:
            self.db.return_book(book_id, user_id)
            tk.messagebox.showinfo(
                    title='Vracanje knjige', message='Uspjesno vracena knjiga')
            self.book_id_entry.delete(0, 'end')
            self.user_id_entry.delete(0, 'end')
        except Exception as e:
            tk.messagebox.showerror(
                title='Greška', message=f'Došlo je do greške: {e}')
       

    def create_menu(self):
        menubar = tk.Menu(self)

        # File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Korisnicki panel", command=self.open_user_panel)
        filemenu.add_separator()
        filemenu.add_command(label="Izlaz", command=self.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        # View menu
        viewmenu = tk.Menu(menubar, tearoff=0)
        viewmenu.add_command(label="Maximize", command=self.maximize_window)
        viewmenu.add_command(label="Minimize", command=self.minimize_window)
        menubar.add_cascade(label="View", menu=viewmenu)

        # Help menu
        helpmenu = tk.Menu(menubar, tearoff=0)
        helpmenu.add_command(label="Pomoć", command=self.show_help)
        helpmenu.add_command(label="O nama", command=self.show_about)
        menubar.add_cascade(label="Help", menu=helpmenu)

        self.config(menu=menubar)

    def maximize_window(self):
        self.state('zoomed')

    def minimize_window(self):
        self.state('iconic')
    def show_help(self):
        messagebox.showinfo("Pomoć", "Ovo je pomoć za dodavanje knjige.")

    def show_about(self):
        messagebox.showinfo("O nama", "Ovo je aplikacija za dodavanje knjiga.")


    def open_user_panel(self):
        from user_panel import KorisnickiPanel
        app = KorisnickiPanel()
        self.destroy()
        app.mainloop()


if __name__ == "__main__":
    db = Database("library_software.db")
    app = ReturnBook(db)
    app.mainloop()
