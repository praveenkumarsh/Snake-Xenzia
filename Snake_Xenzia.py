import argparse
import random
from game.helpers.constants import Constants

## For Play By Human 
from game.models.general_purpose.human_solver import HumanSolver

solvers = [HumanSolver()]

game_models = solvers


def args():
    parser = argparse.ArgumentParser()
    for game_model in game_models:
        parser.add_argument("-"+game_model.abbreviation, "--"+game_model.short_name,
                            help=game_model.long_name,
                            action="store_true")
    return parser.parse_args()


if __name__ == '__main__':
    selected_game_model = random.choice(solvers)
    args = args()
    for game_model in game_models:
        if game_model.short_name in args and vars(args)[game_model.short_name]:
            selected_game_model = game_model
           
    ### Setting Game Property
    from game.game import Game
    Game(game_model=selected_game_model,
    fps=Constants.FPS,
    pixel_size=Constants.PIXEL_SIZE,
    screen_width=Constants.SCREEN_WIDTH,
    screen_height=Constants.SCREEN_HEIGHT+Constants.NAVIGATION_BAR_HEIGHT,
    navigation_bar_height=Constants.NAVIGATION_BAR_HEIGHT)
