'''
Main application file for "Races F1" website.
This file initializes the main window, sets up the tabbed interface,
and loads the different pages (home, Charles Leclerc, Lewis Hamilton).
It uses tkinter for GUI and imports page classes from the 'pages' module.
'''
import tkinter as tk
from tkinter import ttk
from pages.homepage import HomePage
from pages.charlespage import CharlesPage
from pages.lewispage import LewisPage
import styles
class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Races F1")
        self.geometry("800x600")
        self.configure(bg=styles.BACKGROUND_COLOR)
        notebook = ttk.Notebook(self)
        notebook.pack(fill='both', expand=True)
        home_page = HomePage(notebook)
        notebook.add(home_page, text="home")
        charles_page = CharlesPage(notebook)
        notebook.add(charles_page, text="Charles Leclerc")
        lewis_page = LewisPage(notebook)
        notebook.add(lewis_page, text="Lewis Hamilton")
if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()