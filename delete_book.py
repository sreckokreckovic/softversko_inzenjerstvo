import tkinter as tk
import customtkinter as c  

from tkinter import messagebox  
from projekatdb import Database


c.set_appearance_mode("dark")
c.set_default_color_theme("dark-blue")


class DeleteBook(c.CTk):
    def __init__(self, db, master=None):
        super().__init__(master)
        self.db = db
        self.master = master

        self.title("Obriši Knjigu")
        self.geometry("1080x720")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_label = c.CTkLabel(
            self, text="Obrišite knjigu", font=("Verdana", 20))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=30)

        self.frame = c.CTkFrame(self)
        self.frame.grid(row=1, column=0, padx=0, pady=120, sticky='n')

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1, pad=20)
        self.frame.grid_columnconfigure(1, weight=2)

        self.book_id_label = c.CTkLabel(self.frame, text="ID knjige")
        self.book_id_label.grid(row=0, column=0, padx=15, pady=15, sticky='we')

        self.book_id_entry = c.CTkEntry(self.frame, width=300)
        self.book_id_entry.grid(row=0, column=1, padx=15, pady=15, sticky='w')

        self.delete_book_b = c.CTkButton(
            self.frame, text='Obriši knjigu', command=self.delete_book, width=200, font=('Verdana', 15))
        self.delete_book_b.grid(row=1, column=0, columnspan=2, pady=10)

        
        self.create_menu()

    def delete_book(self):
        book_id = self.book_id_entry.get()

        if not book_id:
            tk.messagebox.showerror(
                title='Greška', message='Morate unijeti ID knjige')
            return

        try:
            book_id_int = int(book_id)
            book = self.db.get_book_by_id(book_id_int)
            if not book:
                tk.messagebox.showerror(
                    title='Greška', message='Knjiga sa datim ID-jem ne postoji')
                return
            
            self.db.delete_book(book_id_int)
            tk.messagebox.showinfo(title='Obaveštenje',
                                   message='Knjiga je uspješno obrisana')
            self.book_id_entry.delete(0, 'end')
        except Exception as e:
            tk.messagebox.showerror(
                title='Greška', message=f'Došlo je do greške: {e}')
       

    def create_menu(self):
        menubar = tk.Menu(self)

        # File menu
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Admin panel", command=self.open_admin)
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


    def open_admin(self):
        from admin_panel import Admin
        app = Admin()
        self.destroy()
        app.mainloop()


if __name__ == "__main__":
    db = Database("library_software.db")
    app = DeleteBook(db)
    app.mainloop()
