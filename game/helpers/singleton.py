# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 00:25:25 2019

@author: Praveen
"""


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]