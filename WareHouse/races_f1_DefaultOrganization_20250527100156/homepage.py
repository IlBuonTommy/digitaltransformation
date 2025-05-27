'''
Home page implementation for "Races F1".
Displays the history of Formula 1 with a central panel and red borders.
'''
import tkinter as tk
from styles import BACKGROUND_COLOR, TEXT_COLOR, BORDER_COLOR
class HomePage(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(bg=BACKGROUND_COLOR)
        panel = tk.Frame(self, bg=BORDER_COLOR, bd=2, relief="solid")
        panel.pack(padx=10, pady=10, fill='both', expand=True)
        title = tk.Label(panel, text="home", font=("Arial", 16), fg=TEXT_COLOR, bg=BORDER_COLOR)
        title.pack(pady=5)
        info = tk.Label(panel, text="storia della formula uno", fg=TEXT_COLOR, bg=BORDER_COLOR)
        info.pack(pady=5)
        image_label = tk.Label(panel, text="foto di auto storiche di F1", fg=TEXT_COLOR, bg=BORDER_COLOR)
        image_label.pack()