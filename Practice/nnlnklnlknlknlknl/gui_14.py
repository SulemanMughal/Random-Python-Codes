# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:39:51 2019

@author: SulemanMughal
"""

from tkinter import *



class HelloClass:
    
    
    
    def __init__(self):
        global root
        widget = Button(root, text = "Hello", command = self.quit)
        widget.pack()
        
    def quit(self):
        global root
        print("Hello")
        root.quit()


root  =Tk()

HelloClass()
mainloop()