'''
Main application entry point for the Flower Shop Website GUI.
Initializes the Tkinter application, loads models and views, and starts the GUI loop.
'''
import tkinter as tk
from tkinter import ttk
from flower_model import Flower, flowers_data
from gui_components import create_main_window, setup_product_display, setup_cart_frame
def main():
    # Initialize the main window
    root = create_main_window()
    # Setup product display area
    product_frame = setup_product_display(root)
    # Setup cart frame
    cart_frame = setup_cart_frame(root)
    # Load sample flower data and populate UI
    for flower in flowers_data:
        Flower(flower['name'], flower['price'], flower['image_url'], flower['description'])
    # Start the GUI event loop
    root.mainloop()
if __name__ == "__main__":
    main()