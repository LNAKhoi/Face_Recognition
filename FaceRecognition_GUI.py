import tkinter as tk
from tkinter.font import Font
from typing import Text
from PIL import Image, ImageTk
from pyparsing import col
import cv2

# show webcam frame function

def show_capture_frame():
    camImg= cv2.cvtColor(cap.re)
    img=Image.fromarray(camImg)
    


root= tk.Tk()
# initialize title
root.title("Face Recognition")
root.geometry('400x450')
# initialize Labels frame
application_Title=tk.Label(root,text="Face Recognition",font=Font(family="Poppins",size=20,weight="bold"),fg='lightblue')
application_Title.grid(row=0,column=0)
application_Title.config(anchor=tk.CENTER)
application_Title.pack()

# intialize webcam frame
cap=cv2.VideoCapture(0)
winLabel=tk.Label(root)
winLabel.grid(row=1, column=0)
show_capture_frame()
# initialize logo 

root.mainloop()
