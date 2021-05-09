# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:33:50 2019

@author: SulemanMughal
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:28:44 2019

@author: SulemanMughal
"""

# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 20:14:11 2019

@author: SulemanMughal
"""




from tkinter import *


def user_quit(x):
    print("Goes to Offline : ")

root = Tk()
widget = Button(root, text="Hello GUI World!", command = user_quit(root))
widget.pack(expand = YES, fill = Y)
widget.mainloop()

    