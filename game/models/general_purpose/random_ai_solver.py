# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 02:54:34 2019

@author: Praveen
"""

import random
from game.models.base_game_model import BaseGameModel


class RandomSolver(BaseGameModel):

    def __init__(self):
        BaseGameModel.__init__(self, "Random", "random", "r")

    def move(self, environment):
        BaseGameModel.move(self, environment)
        return random.choice(environment.possible_actions_for_current_action(environment.snake_action))
