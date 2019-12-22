# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 00:21:17 2019

@author: Praveen
"""

class Node:

    point = None
    previous_node = None
    action = None

    def __init__(self, point):
        self.point = point

    def __eq__(self, other):
        return self.point == other.point

    def __hash__(self):
        return hash(str(self.point.x)+str(self.point.y))