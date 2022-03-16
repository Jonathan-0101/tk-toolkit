from tkinter import *
import tkinter as tk


class menuMaker:
    
    def __init__(self, root, buttonList, x, y):
        
        self.buttonList = buttonList
        self.root = root
        self.x = x
        self.y = y

        for i in range(len(buttonList)):
            button = Button(self.root, text=buttonList[i][0], command=lambda i=i : [buttonList[i][1](buttonList[i][2])], width=x, height=y,pady=10, padx=10)
            button.pack(pady=10, padx=10)
