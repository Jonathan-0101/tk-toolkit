import tkinter as tk
from tkinter import *
from tk_toolkit import tk_toolkit

window = tk.Tk()  # Sets up GUI
window.title("Example")  # Titles GUI
window.geometry("1000x1000")  # Sizes GUI

# Webcam object
# Uses Box class from webcam to create video window, if no camera is specified default is used
video = tk_toolkit.Webcam(window, width=450, height=450, camera=1)
video.show_frames()  # Show the created Box

# Menu object


def function1(prameterList1):
    print(prameterList1)


parameter1 = "parameter1"
parameter2 = "parameter2"

# Putting the parameters of the function into a tupple
prameterList1 = (parameter1, parameter2)

# Creating a 2D array for the buttons, with the text for button, function and the parameters
buttonList = [["Button 1", function1, prameterList1]]

# Calling the function, passing through the tkinter window and button list
tk_toolkit.Menu(window, buttonList, 7, 1)

tk.mainloop()
