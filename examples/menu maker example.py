import tkinter as tk
import tkinter_menu as tkm
from tkinter_menu.tkinter_menu import menuMaker

def function1(prameterList1):
    print(prameterList1)

#Creating base window   
root = tk.Tk()
root.geometry('360x500')
root.title('Menu')

parameter1 = "parameter1"
parameter2 = "parameter2"

#Putting the parameters of the function into a tupple
prameterList1 = (parameter1, parameter2)

#Creating a 2D array for the buttons, with the text for button, function and the parameters
buttonList = [["Button 1",function1, prameterList1]]

#Calling the function, passing throught the tkinter window, button list and size for buttons 
tkm.menuMaker(root, buttonList, 4, 1)

root.mainloop()