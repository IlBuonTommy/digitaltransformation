'''
F1WebsiteGenerator class for generating F1 website pages with a GUI interface.
This class handles the main window, buttons for page generation, and status updates.
'''
import webbrowser
from tkinter import *
from tkinter import messagebox
class F1WebsiteGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Races F1 Website Generator")
        self.root.geometry("600x400")
        # Title Label
        Label(root, text="Races F1 Website Generator", font=("Arial", 16)).pack(pady=10)
        # Buttons for generating pages
        Button(root, text="Generate Home Page", command=self.generate_home).pack(pady=5)
        Button(root, text="Generate Charles Leclerc Page", command=self.generate_charles).pack(pady=5)
        Button(root, text="Generate Lewis Hamilton Page", command=self.generate_lewis).pack(pady=5)
        # Status Label
        self.status_label = Label(root, text="", fg="green")
        self.status_label.pack()
    def generate_home(self):
        html_content = generate_home_html()
        with open("home.html", "w") as file:
            file.write(html_content)
        self.status_label.config(text="Home page generated successfully!", fg="green")
        webbrowser.open_new_tab("home.html")
    def generate_charles(self):
        html_content = generate_charles_html()
        with open("charles_leclerc.html", "w") as file:
            file.write(html_content)
        self.status_label.config(text="Charles Leclerc page generated successfully!", fg="green")
        webbrowser.open_new_tab("charles_leclerc.html")
    def generate_lewis(self):
        html_content = generate_lewis_html()
        with open("lewis_hamilton.html", "w") as file:
            file.write(html_content)
        self.status_label.config(text="Lewis Hamilton page generated successfully!", fg="green")
        webbrowser.open_new_tab("lewis_hamilton.html")
if __name__ == "__main__":
    root = Tk()
    app = F1WebsiteGenerator(root)
    root.mainloop()