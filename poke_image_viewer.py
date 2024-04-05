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


# Create frames
frm = ttk.Frame(root)
frm.grid(sticky="nsew")
frm.columnconfigure(0, weight=1)
frm.rowconfigure(0, weight=1)


# Populate frames with widgets and define event handler functions
image_path = os.path.join(script_dir, "poke_ball.png")
photo = PhotoImage(file=image_path)
image_lbl = ttk.Label(frm, image=photo)
image_lbl.grid(row=0, column=0, padx=10, pady=10)

pokemon_list = poke_api.get_pokemon_names()
poke_cbox = ttk.Combobox(frm, values=pokemon_list, state="readonly")
poke_cbox.set("Select a Pokemon")
poke_cbox.grid(row=1, column=0, pady=10)

# select_pokemon function created 
def select_pokemon(event):
    """
    Event handler for the combobox selection event.
    Updates the displayed Pokemon artwork and enables/disables the set desktop button.

    Args:
        event: The event object (not used in this function, but required by the event binding)

    Returns:
        None
    """
    pokemon = poke_cbox.get()
    image_path = poke_api.get_pokemon_art(pokemon, images_dir)
    if image_path:
        photo["file"] = image_path
        image_lbl["text"] = ""
        image_lbl["image"] = photo
        set_desktop_button["state"] = "normal"
    else:
        image_lbl["image"] = None
        image_lbl["text"] = "No artwork available"
        set_desktop_button["state"] = "disabled"

poke_cbox.bind("<<ComboboxSelected>>", select_pokemon)


# set_as_desktop_image function created 
def set_as_desktop_image():
  """
      Event handler for the 'Set as Desktop Image' button.
      Sets the selected Pokemon's artwork as the desktop background image.

      Returns:
          None
  """
  pokemon = poke_cbox.get()
  image_path = poke_api.get_pokemon_art(pokemon, images_dir)
  if image_path:
      ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 0)
      messagebox.showinfo("Success :)", f"{pokemon.capitalize()} image set as Desktop background successfully!")
      print(f"{pokemon.capitalize()} image set as Desktop background successfully")
  else:
      messagebox.showerror("Error", "Failed to set desktop image")
      print("Error!, Failed to set desktop image")

# Create the Set as Desktop Image button
set_desktop_button = ttk.Button(frm, text="Set as Desktop Image", command=set_as_desktop_image, state="disabled")
set_desktop_button.grid(row=2, column=0, pady=10)


root.mainloop()