# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 20:01:12 2019

@author: SulemanMughal
"""


def spy_game(nums):
    code = [0, 0, 7, 'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    
    return len(code) == 1
