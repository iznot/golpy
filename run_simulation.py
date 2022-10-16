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
    

    # check if extinct

    if np.sum(last_gameboard) == 0:
        return "extinct"


    # check if equals

    if gameboard_equal(last_gameboard, previous_gameboard):
        return "stable"
    
    # check if oscillator
    if all_gameboards() == True:
        return "oscilator"

    # check if spaceship
    if compare_neighbours() == True:
        return "spaceship"

    # else
    return 'survival'

def all_gameboards(gameboards):
    length = len(gameboards)
    last_gameboard = gameboards[length-1]
    for i in reversed(gameboards):
        gameboard_equal(last_gameboard, i)

def compare_neighbours(gameboards):
    length = len(gameboards)
    last_gameboard = gameboards[length-1]
    last_neighbours = get_neighbour_indices(last_gameboard)
    for i in reversed(gameboards):
        other_neighbours = get_neighbour_indices(i)
        set(last_neighbours) == set(other_neighbours)



    #counter = sum(1 if x==y else -1 for x, y in product (last_gameboard, i))


