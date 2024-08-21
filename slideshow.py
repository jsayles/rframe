#!/usr/bin/python3
#
# From: https://www.geeksforgeeks.org/create-a-sideshow-application-in-python/
################################################################################

import os
import sys

import tkinter as tk 
from tkinter import *
from PIL import Image 
from PIL import ImageTk 


WAIT_MS = 30000

os.environ["DISPLAY"] = ":0"


def close(event):
    sys.exit()


root=tk.Tk()
root.geometry("1080x1920")
root.attributes('-fullscreen',True)
root.config(cursor="none")
root.bind('<Escape>',close)


img1=ImageTk.PhotoImage(Image.open("/home/jacob/rframe/photos/photo1.jpg")) 
img2=ImageTk.PhotoImage(Image.open("/home/jacob/rframe/photos/photo2.jpg")) 
img3=ImageTk.PhotoImage(Image.open("/home/jacob/rframe/photos/photo3.jpg")) 
img4=ImageTk.PhotoImage(Image.open("/home/jacob/rframe/photos/photo4.jpg")) 

l=Label() 
l.pack() 


x = 1
def move():
    global x
    if x == 5:
        x = 1

    if x == 1:
        l.config(image=img1)
    elif x == 2:
        l.config(image=img2)
    elif x == 3:
        l.config(image=img3)
    elif x == 4:
        l.config(image=img4)

    x = x+1
    root.after(WAIT_MS, move)


move()
root.mainloop()
