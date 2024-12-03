import tkinter as tk
from tkinter import filedialog
import ctypes
import os

def select_and_set_wallpaper():
    # Create and hide the main tkinter window
    root = tk.Tk()
    root.withdraw()

    # Open file browser dialogue
    file_path = filedialog.askopenfilename(
        title="Select Wallpaper Image",
        filetypes=[
            ("Image files", "*.jpg;*.jpeg;*.png;*.bmp"),
            ("All files", "*.*")
        ]
    )

    # Check if a file was selected
    if file_path:
        # Convert to absolute path
        abs_path = os.path.abspath(file_path)
        
        # Set wallpaper (Windows only)
        try:
            ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 0)
            print("Wallpaper set successfully!")
        except Exception as e:
            print(f"Error setting wallpaper: {e}")
    else:
        print("No file selected")

# Run the function
if __name__ == "__main__":
    select_and_set_wallpaper()
