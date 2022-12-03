import numpy as np
from basic_game_functions import gameboard_equal, play
from itertools import product
from basic_game_functions import get_neighbour_indices
import gameboard_manipulation as gam
import basic_game_functions as gm



def run_simulation(gameboard, max_runs):
    gameboards = [gameboard]
    for i in range(1, max_runs):
        gameboard = play(gameboard)
        gameboards.append(gameboard)
        exit_criteria, periodicity = check_exit_criteria(gameboards)
        if exit_criteria != 'survival':
            return gameboards, exit_criteria, periodicity

def check_exit_criteria(gameboards):
    length = len(gameboards)
    last_gameboard = gameboards[length-1]
    previous_gameboard = gameboards[length-2]
    previous_gameboards = gameboards[1:(length-2)]
    

    # check if extinct (all empty)

    if np.sum(last_gameboard) == 0:
        return "extinct", -1


    # check if equals

    if gameboard_equal(last_gameboard, previous_gameboard):
        return "stable", -1
    
    # check if oscillator
    osc_check, periodicity = check_exists(last_gameboard, previous_gameboards)
    if osc_check:
        return "oscilator", periodicity

    # check if spaceship
    lg_cut = gam.cut_both_axis(last_gameboard)
    pg_cut = [gam.cut_both_axis(gb) for gb in previous_gameboards]
    spaceship_check, periodicity = check_exists(lg_cut, pg_cut)
    if spaceship_check:
        return "spaceship", periodicity

    # else
    return 'survival', -1

def check_exists(gameboard_to_check, gameboards):
    length = len(gameboards)
    
    for i in range(length-1, 0, -1):
        gameboard_to_compare = gameboards[i]
        res = gameboard_equal(gameboard_to_check, gameboard_to_compare)
        if res: return True, length - i + 1
    return False, -1





    #counter = sum(1 if x==y else -1 for x, y in product (last_gameboard, i))


def convert_to_string(gameboard):
    
    gb_array = gameboard.ravel()

    gb_bits = gb_array.astype(int)

    # gb_int = bits_to_int(gb_bits)

    gb_str = ''.join(map(str, gb_bits))
    gb_int = int(gb_str, 2)
    gb_hex = hex(gb_int)

    width = len(gameboard[0])
    leading_zeroes= get_leading_zeroes(gb_bits)

    res = f'{width},{leading_zeroes},{gb_hex}'
    return res


def get_leading_zeroes(bits):
    i = np.argmax(bits!=0)
    if i==0 and np.all(bits==0): i=len(bits)
    return i