import numpy as np
from basic_game_functions import gameboard_equal, play
from itertools import product
from basic_game_functions import get_neighbour_indices

def run_simulation(gameboard, max_runs):
    gameboards = [gameboard]
    for i in range(1, max_runs):
        gameboard = play(gameboard)
        gameboards = gameboards.append(gameboard)


def check_exit_criteria(gameboards):
    length = len(gameboards)
    last_gameboard = gameboards[length-1]
    previous_gameboard = gameboards[length-2]
    previous_gameboards = gameboards[1:(length-2)]
    

    # check if extinct

    if np.sum(last_gameboard) == 0:
        return "extinct"


    # check if equals

    if gameboard_equal(last_gameboard, previous_gameboard):
        return "stable"
    
    # check if oscillator
    osc_check, periodicity = check_exists(last_gameboard, previous_gameboards)
    if osc_check:
        return "oscilator", periodicity

    # check if spaceship
    if compare_neighbours(gameboards) == True:
        return "spaceship"

    # else
    return 'survival'

def check_exists(gameboard_to_check, gameboards):
    length = len(gameboards)
    
    for i in range(length-1, 0, -1):
        gameboard_to_compare = gameboards[i]
        res = gameboard_equal(gameboard_to_check, gameboard_to_compare)
        if res: return True, length - i + 1
    return False, -1

def compare_neighbours(gameboards):
    length = len(gameboards)
    last_gameboard = gameboards[length-1]
    last_neighbours = get_neighbour_indices(last_gameboard)
    for i in reversed(gameboards):
        other_neighbours = get_neighbour_indices(i)
        set(last_neighbours) == set(other_neighbours)



    #counter = sum(1 if x==y else -1 for x, y in product (last_gameboard, i))


