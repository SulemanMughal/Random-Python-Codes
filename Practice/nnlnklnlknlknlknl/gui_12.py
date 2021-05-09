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

import sys
from tkinter import *
root = Tk()
widget = Button(root, text="Hello GUI World!", command = root.destroy)
widget.pack(expand = YES, fill = Y)
widget.mainloop()