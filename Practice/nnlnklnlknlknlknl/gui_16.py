# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:52:19 2019

@author: SulemanMughal
"""

from tkinter import *

def greeting():
    print("Hello stdout world!...")
    
    

root = Tk()

win = Frame(root)
win.pack()

Button(win, text="Hello", command = greeting).pack(side=LEFT)
Button(win, text="Quit", command = root.destroy).pack(side = RIGHT)
Label(win, text = "Hello Container World!").pack(side = TOP)
win.mainloop()