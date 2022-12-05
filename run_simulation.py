import numpy as np
from basic_game_functions import gameboard_equal, play
from itertools import product
from basic_game_functions import get_neighbour_indices
import gameboard_manipulation as gam
import basic_game_functions as gm
import csv
import logging



def run_simulation(gameboard, max_runs):
    gameboards = [gameboard]
    for i in range(1, max_runs):
        gameboard = gam.expand_gameboard_if_necessary(gameboard)
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
        return "extinct", 0


    # check if equals

    if gameboard_equal(last_gameboard, previous_gameboard):
        return "stable", 0
    
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
    return 'survival', 0

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
    # IDEA: base64 would be even more efficient than hex.
    # gb_64 = base64.b64encode(gb_bits)

    width = len(gameboard[0])
    leading_zeroes= get_leading_zeroes(gb_bits)

    res = f'{width},{leading_zeroes},{gb_hex}'
    return res


def get_leading_zeroes(bits):
    i = np.argmax(bits!=0)
    if i==0 and np.all(bits==0): i=len(bits)
    return i

def convert_to_gameboard(gameboard_str):
    res_list = gameboard_str.split(',')
    width = int(res_list[0])
    leading_zeroes = int(res_list[1])
    gb_hex_str = res_list[2]

    gb_int = int(gb_hex_str, 16)
    gb_bin = bin(gb_int)[2:]
    gb_bin = gb_bin.zfill(len(gb_bin) + leading_zeroes)
    gb_array_1D = np.fromstring(gb_bin,'u1') - ord('0')
    gb_array_2D = np.reshape(gb_array_1D, (-1, width))
    gameboard = gb_array_2D.astype(bool)

    return gameboard


#generate csv file


def generate_simulation(rows,cols,max_runs):
    cells = rows * cols
    max_value = (2**cells)-1

    results_header = ['start_gameboard', 'end_gameboard', 'exit_criteria', 'periodicity', 'rows', 'cols', 'max_height', 'max_width']

    with open('simulation_results.csv', 'w',  newline='') as file:
        writer = csv.writer(file)
        writer.writerow(results_header)

        gameboard_sim_start_history = []

        for gameboard_int in range(max_value):

            gb_bin = bin(gameboard_int)[2:]
            gb_bin = gb_bin.zfill(cells)
            gb_array_1D = np.fromstring(gb_bin,'u1') - ord('0')
            gb_array_2D = np.reshape(gb_array_1D, (rows, cols))
            gameboard = gb_array_2D.astype(bool)
            
                    

            # check if current gb is in history
                # NOTE: debug only
           # already_simulated = check_similar_exists(gameboard_sim_start_history, gameboard)

            #if already_simulated:
             #  continue              


            gameboards, exit_criteria, periodicity = run_simulation(gameboard, max_runs)

            start_gameboard = convert_to_string(gameboard)
            end_gameboard = convert_to_string(gameboards[len(gameboards)-1])

            max_height= np.shape(gameboards[len(gameboards)-1])[0]
            max_width = np.shape(gameboards[len(gameboards)-1])[1]
    
            new_row = [start_gameboard, end_gameboard, exit_criteria, periodicity, rows, cols, max_height, max_width]

            writer.writerow(new_row)

            if gameboard_int % 100 == 0:
                print(f'{gameboard_int}/{max_value} {100*gameboard_int//max_value}%')

def check_similar_exists(gameboard_sim_start_history, gameboard):
    existence = False
    cut_gb = gam.cut_both_axis(gameboard)
    for past_gameboard in gameboard_sim_start_history:
        existence = gameboard_equal(cut_gb,past_gameboard)
        if existence:
            break
    
    gameboard_sim_start_history.append(cut_gb)
    return existence

        
    
