# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:04:51 2019

@author: SulemanMughal
"""

import tkinter as tk

# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
# import Tkinter as tk

root = tk.Tk()

w = tk.Label(root, text="Hello Tkinter!")
w.pack()

root.mainloop()