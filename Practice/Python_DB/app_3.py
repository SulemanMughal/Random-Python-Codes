import mysql.connector as view
import cgi


from tkinter import *
from tkinter.messagebox import *
import Pmw


class AddressBOok(Frame):

    def __init__(self):
        Frame.__init__(self)
        Pmw.initialise()
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Address Book Database Application")

        self.buttons = Pmw.ButtonBox(self, padx=0)
        self.buttons.grid(columnspan = 2)
        self.buttons.add("Find", command = self.findAddress)
        self.
        
