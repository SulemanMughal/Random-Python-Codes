# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:47:06 2019

@author: SulemanMughal
"""

from tkinter import *
root = Tk()

def hello(event):
    print("Press Twice to exit")

def quit_1(event):
    global root
    print("Hello, I must be going")
    root.destroy


widget = Button(root, text="Hello")
widget.pack()
widget.bind('<Button-1>', hello)
widget.bind('<Double-1>', quit_1)
widget.mainloop()