# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:03:49 2019

@author: SulemanMughal
"""

from tkinter import *
root= Tk()
widget = Label(root)
widget.config(text="Hello GUI World!")
widget.pack(side=TOP, expand = YES, fill = BOTH)
root.title("GUI Build")
root.mainloop()