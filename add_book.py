import tkinter as tk
import customtkinter as c
from tkinter import messagebox  
from projekatdb import Database
from login import Login

c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")


class AddBook(c.CTk):
    def __init__(self, db, master=None):
        super().__init__(master)
        self.db = db
        self.master = master

        self.title("Softver za biblioteku")
        self.iconbitmap("books_97178.ico")
        self.geometry("1080x720")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_label = c.CTkLabel(
            self, text="Dodajte novu knjigu", font=("Verdana", 30))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        self.frame = c.CTkFrame(self)
        self.frame.grid(row=1, column=0, padx=10, pady=20, sticky='n')

        for i in range(7):
            self.frame.grid_rowconfigure(i, weight=1)
            self.frame.grid_columnconfigure(0, weight=1, pad=100)
            self.frame.grid_columnconfigure(1, weight=2)
        
        self.name = self.create_elements(self.frame, "Naziv knjige", 0)
        self.author = self.create_elements(self.frame, "Autor", 1)
        self.year = self.create_elements(self.frame, "Godina", 2)
        self.description = self.create_elements(self.frame, "Opis", 3)
        self.available = self.create_elements(self.frame, "Dostupnost", 4)

        self.genre_label = c.CTkLabel(self.frame, text="Žanr")
        self.genre_label.grid(row=5, column=0, padx=15, pady=1, sticky='we')

        self.genre_var = tk.StringVar()
        genres = ["Naučna fantastika", "Misterija", "Biografija", "Fantazija"]
        for i, genre in enumerate(genres):
            radio = c.CTkRadioButton(self.frame, text=genre, variable=self.genre_var, value=genre)
            radio.grid(row=5 + i, column=1, padx=15, pady=5, sticky='w')

        self.add_book_b = c.CTkButton(
            self.frame, text='Dodaj knjigu', command=self.add_book, width=180, font=('Verdana', 15))
        self.add_book_b.grid(row=10, column=0, columnspan=2, pady=10)

        self.button_frame = c.CTkFrame(self)
        self.button_frame.grid(row=2, column=0, columnspan=2, pady=30)
        self.show_main = c.CTkButton(
            self.button_frame, text="Početna", font=('Verdana', 15), width=180, command=self.open_main)
        self.show_main.grid(row=0, column=0, padx=10)

        self.create_menu()

    def create_menu(self):
        menubar = tk.Menu(self)

        # File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Početna", command=self.open_main)
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

    def add_book(self):
        name = self.name.get()
        author = self.author.get()
        year = self.year.get()
        description = self.description.get()
        available = self.available.get()
        genre = self.genre_var.get()

        if not name or not author or not year or not available or not genre:
            tk.messagebox.showerror(
                title='Greška', message='Morate popuniti sva polja')
            return

        try:
            self.db.add_book(name, author, int(year), description, int(available), genre)
            tk.messagebox.showinfo(title='Obavještenje',
                                   message='Knjiga je uspješno dodata')
            self.clear_all()
        except Exception as e:
            tk.messagebox.showerror(
                title='Greška', message=f'Došlo je do greške: {e}')

    def clear_all(self):
        self.name.delete(0, 'end')
        self.author.delete(0, 'end')
        self.year.delete(0, 'end')
        self.description.delete(0, 'end')
        self.available.delete(0, 'end')
        self.genre_var.set('')

    def create_elements(self, frame, text, row, show=None):
        label = c.CTkLabel(frame, text=text)
        label.grid(row=row, column=0, padx=15, pady=15, sticky='we')
        entry = c.CTkEntry(frame, width=300, show=show)
        entry.grid(row=row, column=1, padx=15, pady=15, sticky='w')
        return entry

    def open_main(self):
        from main import Pocetni
        app = Pocetni()
        self.destroy()
        app.mainloop()

    def show_help(self):
        messagebox.showinfo("Pomoć", "Ovo je pomoć za dodavanje knjige.")

    def show_about(self):
        messagebox.showinfo("O nama", "Ovo je aplikacija za dodavanje knjiga.")

if __name__ == "__main__":
    db = Database("library_software.db")
    app = AddBook(db)
    app.mainloop()
