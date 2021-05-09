# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 08:43:06 2019

@author: SulemanMughal
"""

from . import Animal

class Dog(Animal):
    
    def __init__(self):
        Animal.__init__(self)
        print("Dog Created!")
        
    def who_am_i(self):
        print("I am a Dog!")
    
    def bark(self):
        print('Woff!')

    def 