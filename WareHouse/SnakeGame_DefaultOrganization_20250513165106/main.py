'''
Snake Website Main Application
This is the main application for the snake website. It creates a GUI window with:
- A title
- Introduction section
- List of interesting facts
- Fun fact section
- Image of a snake
'''
import tkinter as tk
from tkinter import ttk, PhotoImage
import os
from snake_data import snake_content
class SnakeWebsiteApp:
    def __init__(self, root):
        '''
        Initialize the main application window
        Parameters:
            root (tk.Tk): The main Tkinter window
        '''
        self.root = root
        self.root.title("Il Serpente - Informazioni")
        self.root.geometry("600x500")
        # Create a frame for the content
        self.content_frame = ttk.Frame(self.root, padding="20")
        self.content_frame.grid(row=0, column=0, sticky="nsew")
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.content_frame.columnconfigure(0, weight=1)
        # Configure content frame rows for proper sizing
        self.content_frame.rowconfigure(0, weight=0)  # Title row (fixed height)
        self.content_frame.rowconfigure(1, weight=1)  # Introduction (expandable)
        self.content_frame.rowconfigure(2, weight=0)  # Facts label (fixed height)
        self.content_frame.rowconfigure(3, weight=1)  # Facts list (expandable)
        self.content_frame.rowconfigure(4, weight=0)  # Fun fact label (fixed height)
        self.content_frame.rowconfigure(5, weight=1)  # Fun fact text (expandable)
        self.content_frame.rowconfigure(6, weight=1)  # Image section (expandable)
        # Create the title label
        self.create_title()
        # Create the introduction section
        self.create_introduction()
        # Create the facts section
        self.create_facts()
        # Create the fun fact section
        self.create_fun_fact()
        # Create the image section
        self.create_image()
    def create_title(self):
        '''
        Create the main title for the website
        '''
        title_label = ttk.Label(
            self.content_frame,
            text="Il Serpente - Informazioni",
            font=("Arial", 20, "bold"),
            anchor="center"
        )
        title_label.grid(row=0, column=0, pady=(0, 15), sticky="ew")
    def create_introduction(self):
        '''
        Create the introduction section with text
        '''
        intro_text = tk.Text(
            self.content_frame,
            wrap=tk.WORD,
            font=("Arial", 12),
            height=4,
            borderwidth=0,
            highlightthickness=0
        )
        intro_text.insert(tk.END, snake_content['introduction'])
        intro_text.configure(state="disabled")
        intro_text.grid(row=1, column=0, pady=(0, 15), sticky="nsew")
    def create_facts(self):
        '''
        Create the section displaying interesting facts
        '''
        facts_label = ttk.Label(
            self.content_frame,
            text="Fatti interessanti sui serpenti:",
            font=("Arial", 14, "bold")
        )
        facts_label.grid(row=2, column=0, pady=(15, 5), sticky="w")
        # Create a frame for the facts list
        facts_frame = ttk.Frame(self.content_frame)
        facts_frame.grid(row=3, column=0, sticky="nsew")
        # Add each fact to the frame
        for i, fact in enumerate(snake_content['facts']):
            fact_label = ttk.Label(
                facts_frame,
                text=f"- {fact}",
                font=("Arial", 12),
                wraplength=550
            )
            fact_label.grid(row=i, column=0, pady=(5, 0), sticky="w")
    def create_fun_fact(self):
        '''
        Create the fun fact section with text
        '''
        fun_fact_label = ttk.Label(
            self.content_frame,
            text="Fatto divertente:",
            font=("Arial", 14, "bold")
        )
        fun_fact_label.grid(row=4, column=0, pady=(15, 5), sticky="w")
        fun_fact_text = tk.Text(
            self.content_frame,
            wrap=tk.WORD,
            font=("Arial", 12),
            height=3,
            borderwidth=0,
            highlightthickness=0
        )
        fun_fact_text.insert(tk.END, snake_content['fun_fact'])
        fun_fact_text.configure(state="disabled")
        fun_fact_text.grid(row=5, column=0, pady=(0, 15), sticky="nsew")
    def create_image(self):
        '''
        Create the section displaying a snake image
        '''
        # Check if the image file exists
        if os.path.exists(snake_content['image_path']):
            try:
                image = PhotoImage(file=snake_content['image_path'])
                image_label = ttk.Label(self.content_frame, image=image)
                image_label.image = image  # Keep reference to prevent garbage collection
                image_label.grid(row=6, column=0, pady=(15, 0), sticky="nsew")
            except Exception as e:
                error_label = ttk.Label(
                    self.content_frame,
                    text=f"Errore nel caricamento dell'immagine: {str(e)}",
                    foreground="red"
                )
                error_label.grid(row=6, column=0, pady=(15, 0), sticky="nsew")
        else:
            error_label = ttk.Label(
                self.content_frame,
                text=f"Immagine non trovata: {snake_content['image_path']}",
                foreground="red"
            )
            error_label.grid(row=6, column=0, pady=(15, 0), sticky="nsew")