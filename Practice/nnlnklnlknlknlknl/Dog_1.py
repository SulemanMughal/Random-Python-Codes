# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 12:16:25 2019

@author: SulemanMughal
"""

class Dog():
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def sit(self):
        print(self.name.title() + " is now sitting.")
    
    def roll_over(self):
        print(self.name.title() + " rolled over!")
    
    