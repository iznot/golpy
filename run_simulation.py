import numpy as np
from basic_game_functions import gameboard_equal, play

def run_simulation(gameboard, max_runs):
    gameboards = [gameboard]
    for i in range(1, max_runs):
        gameboard = play(gameboard)
        gameboards = gameboards.append(gameboard)


def check_exit_criteria(gameboards):
    length = len(gameboards)
    last_gameboard = gameboards[length-1]
    previous_gameboard = gameboards[length-2]


    # check if extinct

    if np.sum(last_gameboard) == 0:
        return "extinct"


    # check if equals

    if gameboard_equal(last_gameboard, previous_gameboard):
        return "stable"
    


    # check if oscillator



    # else
    return 'survival'