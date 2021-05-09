# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 21:23:50 2019

@author: SulemanMughal
"""

import tkinter

window = tkinter.Tk()
window.title("GUI")

# creating a function called say_hi()
def say_hi():
    tkinter.Label(window, text = "Hi").pack()

tkinter.Button(window, text = "Click Me!", command = say_hi).pack() # 'command' is executed when you click the button
                                                                    # in this above case we're calling the function 'say_hi'.
window.mainloop()