import tkinter as tk
from tkinter import *
from tk_toolkit import tk_toolkit

window = tk.Tk() # Sets up GUI
window.title("Example") # Titles GUI
window.geometry("1000x1000") # Sizes GUI

# Webcam object
video = tk_toolkit.Webcam(window, 450, 450) # Uses Box class from webcam to create video window
video.show_frames() # Show the created Box

# Menu object
def function1(prameterList1):
    print(prameterList1)

parameter1 = "parameter1"
parameter2 = "parameter2"

prameterList1 = (parameter1, parameter2) # Putting the parameters of the function into a tupple

buttonList = [["Button 1",function1, prameterList1]] # Creating a 2D array for the buttons, with the text for button, function and the parameters

tk_toolkit.Menu(window, buttonList, 7, 1) # Calling the function, passing through the tkinter window and button list

tk.mainloop()