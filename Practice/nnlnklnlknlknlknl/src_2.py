# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 02:16:20 2019

@author: SulemanMughal
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 16:04:51 2019

@author: SulemanMughal
"""

from tkinter import *

# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
# import Tkinter as tk

window = Tk()
#print(dir(Tk))


#print(Button?)

btn = Button(window, text="Execute")

btn.pack()

#btn.grid()
#btn.grid(row = 5,column = 10)

e1= Entry(window)
e1.pack()


t1 = Text(window)
t1.pack()
window.mainloop()