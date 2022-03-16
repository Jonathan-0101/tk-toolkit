import tkinter as tk
from tkinter import *
from tk_toolkit import tk_toolkit

window = tk.Tk() # Sets up GUI
window.title("Example") # Titles GUI
window.geometry("1000x1000") # Sizes GUI

# Webcam
video = tk_toolkit.Webcam(window, 450, 450) # Uses Box class from webcam to create video window
video.show_frames() # Show the created Box

tk.mainloop()