# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 00:22:39 2019

@author: Praveen
"""


class Queue:

    def __init__(self, initial_values):
        self.queue = initial_values

    def enqueue(self, val):
        self.queue.insert(0, val)

    def dequeue(self):
        if self.is_empty():
            return None
        else:
            return self.queue.pop()

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return self.size() == 0