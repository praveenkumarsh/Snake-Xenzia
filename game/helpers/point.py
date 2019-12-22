# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 00:22:20 2019

@author: Praveen
"""


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(str(self.x)+str(self.y))