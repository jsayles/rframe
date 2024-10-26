#!/usr/bin/python3

import os
import sys
import board
import tkinter as tk

from tkinter import Label
from PIL import Image
from PIL import ImageTk
from adafruit_seesaw import seesaw, rotaryio, digitalio


WAIT_MS = 30000

os.environ["DISPLAY"] = ":0"

i2c = board.I2C()  # uses board.SCL and board.SDA
seesaw = seesaw.Seesaw(i2c, addr=0x36)
seesaw_product = (seesaw.get_version() >> 16) & 0xFFFF
print("Found product {}".format(seesaw_product))
if seesaw_product != 4991:
    print("Wrong firmware loaded?  Expected 4991")

# Configure seesaw pin used to read knob button presses
# The internal pull up is enabled to prevent floating input
seesaw.pin_mode(24, seesaw.INPUT_PULLUP)
button = digitalio.DigitalIO(seesaw, 24)

button_held = False

encoder = rotaryio.IncrementalEncoder(seesaw)
last_position = None


def close(event):
    sys.exit()


root = tk.Tk()
root.geometry("1080x1920")
root.attributes("-fullscreen", True)
root.config(cursor="none")
root.bind("<Escape>", close)


img1 = ImageTk.PhotoImage(Image.open("/home/jacob/rframe/photos/photo1.jpg"))
img2 = ImageTk.PhotoImage(Image.open("/home/jacob/rframe/photos/photo2.jpg"))
img3 = ImageTk.PhotoImage(Image.open("/home/jacob/rframe/photos/photo3.jpg"))
img4 = ImageTk.PhotoImage(Image.open("/home/jacob/rframe/photos/photo4.jpg"))

label = Label()
label.pack()



while True:
    # negate the position to make clockwise rotation positive
    position = -encoder.position

    if position != last_position:
        last_position = position
        print("Position: {}".format(position))

    if not button.value and not button_held:
        button_held = True
        print("Button pressed")

    if button.value and button_held:
        button_held = False
        print("Button released")

def move():
    global x
    if x == 5:
        x = 1

    if x == 1:
        label.config(image=img1)
    elif x == 2:
        label.config(image=img2)
    elif x == 3:
        label.config(image=img3)
    elif x == 4:
        label.config(image=img4)

    x = x + 1
    root.after(WAIT_MS, move)


move()
root.mainloop()
