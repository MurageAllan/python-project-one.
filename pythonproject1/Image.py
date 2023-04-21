from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image, ImageTk
import os

def showimage():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image file", filetype=(("JPG File", "*.jpg"), ("PNG file", "*.png"),("All file", "how are you .txt")))
    img = Image.open(filename)
    img = Image.photoImage(img)
    Lb1.configure(image=img)
    Lb1.image = img
root = Tk()

frame = Frame(root)
frame.pack(side=BOTTOM, padx=15, pady=15)

Lb1 = Label(root)
Lb1.pack()

btn = Button(frame, text="Select Image", command=showimage)
btn.pack(side=tk.LEFT)

btn2 = Button(frame, text="Select Image", command=lambda :exit())
btn2.pack(side=tk.LEFT, padx=12)


root.title("Image Viewer")
root.geometry("400x450")




root.mainloop()