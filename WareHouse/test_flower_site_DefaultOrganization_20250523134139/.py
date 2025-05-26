'''
GUI components module containing functions to create and configure the main application window.
'''
import tkinter as tk
from tkinter import ttk
def create_main_window():
    '''Create and return the main application window.'''
    root = tk.Tk()
    root.title("Flower Shop Website")
    root.geometry("1000x600")
    root.configure(bg="#f5f5f5")
    # Style configuration for modern look
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 10), padding=6)
    style.configure("Header.TLabel", font=("Helvetica", 16, "bold"))
    return root
def setup_product_display(root):
    '''Create and return the product display frame.'''
    product_frame = ttk.Frame(root, padding=(20, 10))
    product_frame.grid(row=0, column=0, sticky="nsew")
    # Product grid layout
    for i, flower in enumerate(Flower.flowers_data):
        product_card = ttk.Label(product_frame, text=f"{flower['name']} - ${flower['price']}", 
                                padding=(10, 5), relief=tk.RAISED)
        product_card.grid(row=i//3, column=i%3, padx=10, pady=10)
    return product_frame
def setup_cart_frame(root):
    '''Create and return the shopping cart frame.'''
    cart_frame = ttk.Frame(root, padding=(20, 10))
    cart_frame.grid(row=0, column=1, sticky="nsew")
    # Cart header
    cart_header = ttk.Label(cart_frame, text="Shopping Cart", style="Header.TLabel")
    cart_header.pack(pady=(0, 10))
    # Cart items list
    cart_list = tk.Listbox(cart_frame, width=50)
    cart_list.pack(fill=tk.BOTH, expand=True)
    return cart_frame