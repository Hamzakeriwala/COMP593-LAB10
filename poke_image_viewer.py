"""
Description:
  Graphical user interface that displays the official artwork for a
  user-specified Pokemon, which can be set as the desktop background image.

Usage:
  python poke_image_viewer.py
"""
from tkinter import *
from tkinter import ttk, PhotoImage, messagebox
import os
import ctypes
import poke_api

# Get the script and images directory
script_dir = os.path.dirname(os.path.abspath(__file__))
images_dir = os.path.join(script_dir, 'images')

# Create the images directory if it does not exist
if not os.path.isdir(images_dir):
    os.makedirs(images_dir)

# Create the main window
root = Tk()
root.title("Pokemon Viewer")
root.minsize(500, 600)
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Set the icon
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("COMP593.PokeImageViewer")
root.iconbitmap(os.path.join(script_dir, "poke_ball.ico"))


# TODO: Create frames

# TODO: Populate frames with widgets and define event handler functions

root.mainloop()