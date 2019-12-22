# -*- coding: utf-8 -*-
"""
Created on Sat Dec 21 23:45:25 2019

@author: Praveen
"""

class Constants:

    SLITHERIN_NAME = "Snake Master"
    ICON_PATH = "./assets/snake-master.png"
    FONT = "Arial"
    MODEL_FEATURE_COUNT = 5 #[action_vector, left_neighbor_accessible, top_neighbor_accessible, right_point_accessible, self.get_angle_from_fruit()]
    NAVIGATION_BAR_HEIGHT = 30
    FPS = 300
    PIXEL_SIZE = 25
    SCREEN_WIDTH = 300
    SCREEN_HEIGHT = 300
    FRAMES_TO_REMEMBER = 4
    SCREEN_DEPTH = 32
    ENV_HEIGHT = SCREEN_HEIGHT/PIXEL_SIZE
    ENV_WIDTH = SCREEN_WIDTH/PIXEL_SIZE