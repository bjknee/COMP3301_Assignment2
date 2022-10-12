import cv2 as cv
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
import random
from random import randint
import numpy as np

global CURRENT_CANVAS_CONTEXT
"""
    Author: Brian Knee
    Student ID: 202050456
    COMP3301 Assignment 1
    SETUP:
    To launch the program:
    Using the program:
    Known Bugs:
"""


def main():
    global CURRENT_CANVAS_CONTEXT
    window = Tk()
    window.title('COMP3301 Assignment 1 - Brian Knee (202050456)')
    window.geometry("615x307")
    raw_image, raw_image_text = open_image_file()

    place_images(raw_image, raw_image)

    original = Button(master=window,
                      command=lambda: add_noise(raw_image_text),
                      height=2,
                      width=10,
                      text="Add Noise")
    original.place(x=10, y=260)

    hist_stretch = Button(master=window,
                          command="",
                          height=2,
                          width=10,
                          text="5x5 Triangle")
    hist_stretch.place(x=110, y=260)

    agg_stretch = Button(master=window,
                         command="",
                         height=2,
                         width=10,
                         text="5x5 Gaussian")
    agg_stretch.place(x=210, y=260)

    hist_equal = Button(master=window,
                        command="",
                        height=2,
                        width=10,
                        text="5x5 Median")
    hist_equal.place(x=325, y=260)

    pdf_view_button = Button(master=window,
                             command="",
                             height=2,
                             width=10,
                             text="5x5 Kuwahara")
    pdf_view_button.place(x=425, y=260)

    close_application = Button(master=window,
                               command=lambda: quit_application(window),
                               height=2,
                               width=10,
                               text="Close\nApplication")
    close_application.place(x=525, y=260)

    window.mainloop()

def add_noise(raw_image_text):
    img = Image.open(raw_image_text)
    width = img.width
    height = img.height
    value = 35
    for i in range(height):
        for j in range(width):
            pixel = img.getpixel((j, i))
            random_int = random.randint(0,70)
            if(random_int > value):
                red = pixel[0]-random_int
                green = pixel[1]-random_int
                blue = pixel[2]-random_int
                img.putpixel((j, i),(red, green, blue))
    original_image = Image.open(raw_image_text)
    place_images(original_image, img)


def place_images(image_one, image_two):
    tk_image = ImageTk.PhotoImage(image_one)
    image_slot = tk.Label(image=tk_image)
    image_slot.image = tk_image
    image_slot.place(x=10, y=0)

    tk_image_alt = ImageTk.PhotoImage(image_two)
    image_slot = tk.Label(image=tk_image_alt)
    image_slot.image = tk_image_alt
    image_slot.place(x=349, y=0)

    return image_slot.image


def open_image_file():
    text = tk.filedialog.askopenfilename()
    image = Image.open(text)
    return (image, text)


def quit_application(window):
    window.quit()


main()