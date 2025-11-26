import tkinter as tk
from tkinter import ttk  # ttk provides modern, themed widgets

# --- 1. INITIALIZE THE MAIN WINDOW ---
# This class structure is the most common and robust way to build a Tkinter app.
class SimpleGUI(tk.Tk):
    def __init__(self):
        super().__init__() # Initialize the tk.Tk parent class
        
        self.title("My Custom GUI") # Sets the text in the title bar
        self.geometry("400x300")   # Sets the default window size (Width x Height)
        
        # Call a method to create and place the UI elements
        self.create_widgets()

    # --- 2. POPULATE & 3. LAYOUT THE WIDGETS ---
    def create_widgets(self):
        # Create a Label widget (used for displaying text/images)
        greeting_label = ttk.Label(self, text="Hello, Tkinter User!")
        
        # Create a Button widget
        my_button = ttk.Button(self, text="Exit Application", command=self.destroy)
        # 'command=self.destroy' links the button click to closing the window.

        # Use the 'pack' geometry manager for simple centering/stacking
        # pady adds vertical padding (space above and below)
        greeting_label.pack(pady=20)
        my_button.pack(pady=10)

# --- EXECUTION BLOCK ---
if __name__ == "__main__":
    # Create an instance of the class (your application)
    app = SimpleGUI()
    
    # Start the main event loop. This line MUST be the last line in your program.
    # It keeps the window open and running until the user closes it.
    app.mainloop()