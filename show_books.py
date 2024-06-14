import tkinter as tk
import customtkinter as ctk
from projekatdb import Database
from admin_panel import Admin
from user_panel import KorisnickiPanel

class ShowBooks(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Softver za biblioteku")
        self.geometry("1080x720")

        self.show_book_list()
        

    def show_book_list(self):
        books_window = BookListWindow(self)
        books_window.pack(side=tk.LEFT, fill=tk.BOTH)

class BookListWindow(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master
        self.create_widgets()

    def create_widgets(self):
        self.canvas = ctk.CTkCanvas(self)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = ctk.CTkScrollbar(self, orientation=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.frame = ctk.CTkFrame(self.canvas)
        self.canvas.create_window((0, 0), window=self.frame, anchor=tk.NW)

        self.frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        books = self.fetch_books_from_database()
        for i, book in enumerate(books):
            self.create_book_entry(book)

        self.canvas.bind_all("<MouseWheel>", lambda event: self.canvas.yview_scroll(-1 * (event.delta // 120), "units"))

    def fetch_books_from_database(self):
        db = Database("library_software.db")
        books = db.available_books()

        books_list = []
        for book in books:
            book_dict = {
                'book_id': book[0],
                'name': book[1],
                'author': book[2],
                'year': book[3],
                'genre': book[6],
                'availability': "Dostupna" if book[5] == 1 else "Nedostupna"
            }
            books_list.append(book_dict)

        return books_list

    def create_book_entry(self, book):
        book_frame = ctk.CTkFrame(self.frame)
        book_frame.pack(padx=20, pady=10, fill=tk.X)

        book_id_label = ctk.CTkLabel(book_frame, text=f"ID: {book['book_id']}", font=("Verdana", 12, "bold"))
        book_id_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        book_name_label = ctk.CTkLabel(book_frame, text=f"Naziv: {book['name']}", font=("Verdana", 12))
        book_name_label.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        book_author_label = ctk.CTkLabel(book_frame, text=f"Autor: {book['author']}", font=("Verdana", 12))
        book_author_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        book_year_label = ctk.CTkLabel(book_frame, text=f"Godina: {book['year']}", font=("Verdana", 12))
        book_year_label.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        book_genre_label = ctk.CTkLabel(book_frame, text=f"Žanr: {book['genre']}", font=("Verdana", 12))
        book_genre_label.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

        availability_label = ctk.CTkLabel(book_frame, text=f"Dostupnost: {book['availability']}", font=("Verdana", 12))
        availability_label.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky=tk.W)

if __name__ == "__main__":
    app = ShowBooks()
    app.mainloop()
