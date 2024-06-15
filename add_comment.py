# -*- coding: utf-8 -*-
"""
Created on Sat Jun 15 02:13:05 2024

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


class AddComment(c.CTk):
    def __init__(self, db, master=None):
        super().__init__(master)
        self.db = db
        self.master = master
        self.iconbitmap("books_97178.ico")

        self.title("Softver za biblioteku")
        self.geometry("1080x720")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_label = c.CTkLabel(
            self, text="Napisi komentar", font=("Verdana", 20))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=30)

        self.frame = c.CTkFrame(self)
        self.frame.grid(row=1, column=0, padx=0, pady=120, sticky='n')

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1, pad=20)
        self.frame.grid_columnconfigure(1, weight=2)
        
        self.comment_title = c.CTkLabel(self.frame, text="Naslov")
        self.comment_title.grid(row=0, column=0, padx=15, pady=15, sticky='we')

        self.comment_title_entry = c.CTkEntry(self.frame, width=300)
        self.comment_title_entry.grid(row=0, column=1, padx=15, pady=15, sticky='w')

        self.comment_text_label = c.CTkLabel(self.frame, text="Komentar:")
        self.comment_text_label.grid(row=1, column=0, padx=15, pady=15, sticky='we')

        self.comment_text_entry = c.CTkEntry(self.frame, width=300)
        self.comment_text_entry.grid(row=1, column=1, padx=15, pady=15, sticky='w')

        self.add_comment_b = c.CTkButton(
            self.frame, text='Posalji', command=self.add_comment, width=200, font=('Verdana', 15))
        self.add_comment_b.grid(row=2, column=0, columnspan=2, pady=10)

        
        self.create_menu()

    def add_comment(self):
        title = self.comment_title_entry.get()
        text = self.comment_text_entry.get() 

        if not title or not text:
            tk.messagebox.showerror(
                title='Greška', message='Morate popuniti sva polja')
            return

        try:
            self.db.add_comment(title,text)
            tk.messagebox.showinfo(
                    title='Komentar', message='Komentar je uspjesno poslat')
            self.comment_title_entry.delete(0, 'end')
            self.comment_text_entry.delete(0, 'end')
        except Exception as e:
            tk.messagebox.showerror(
                title='Greška', message=f'Došlo je do greške: {e}')
       

    def create_menu(self):
        menubar = tk.Menu(self)

        # File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="User panel", command=self.open_user_panel)
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
        messagebox.showinfo("Pomoć", "")

    def show_about(self):
        messagebox.showinfo("O nama", "")


    def open_user_panel(self):
        from user_panel import KorisnickiPanel
        app = KorisnickiPanel()
        self.destroy()
        app.mainloop()


if __name__ == "__main__":
    db = Database("library_software.db")
    app = AddComment(db)
    app.mainloop()
