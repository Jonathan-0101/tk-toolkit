"""tk-toolkit"""
from tkinter import Label, Button
import cv2
from PIL import Image, ImageTk


class Webcam:
    """Webcam"""

    def __init__(self, window, width=450, height=450, camera=0):
        self.window = window
        self.width = width
        self.height = height
        self.camera = camera
        self.label = Label(self.window, width=self.width, height=self.height)
        self.cap = cv2.VideoCapture(camera)
        self.label.pack()

    def show_frames(self):  # Define function to show frame
        """Show Frames"""
        # Get the latest frame and convert into Image
        cv2image = cv2.cvtColor(self.cap.read()[1], cv2.COLOR_BGR2RGB)
        img = Image.fromarray(cv2image)

        imgtk = ImageTk.PhotoImage(image=img)  # Convert image to PhotoImage

        self.label.imgtk = imgtk
        self.label.configure(image=imgtk)

        # Repeat after an interval to capture continiously
        self.label.after(20, self.show_frames)

    def get_info(self):
        """Get Info"""
        print(f"Width: {self.width}")
        print(f"Height: {self.height}")
        print(f"Camera: {self.camera}")


class Menu:
    """Menu"""

    def __init__(self, window, button_list, x, y):

        self.button_list = button_list
        self.window = window
        self.x = x
        self.y = y

        for button_item in button_list:
            button = Button(self.window, text=button_item[0], command=lambda: [
                            button_item[1](button_item[2])], width=x, height=y, pady=10, padx=10)
            button.pack(pady=10, padx=10)

    def change_window(self, new_window):
        """Change Window"""
        self.window = new_window

    def get_info(self):
        """Get Info"""
        print(f"List: {self.button_list}")
        print(f"x: {self.x}")
        print(f"y: {self.y}")
