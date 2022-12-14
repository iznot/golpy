import numpy as np
from basic_game_functions import gameboard_equal, play
from itertools import product
from basic_game_functions import get_neighbour_indices
import gameboard_manipulation as gam
import basic_game_functions as gm

import csv
import datetime as dt



def run_simulation(gameboard, max_runs):
    
    gameboards = [gameboard]
    for i in range(1, max_runs):
        #NOTE: notwendig vorher, falls Anfangsposition am Rand
        gameboard = gam.expand_gameboard_if_necessary(gameboard)
        gameboard = play(gameboard)
        gameboard = gam.cut_both_axis(gameboard)
        gameboards.append(gameboard)
        exit_criteria, periodicity = check_exit_criteria(gameboards)
        if exit_criteria != 'survival':
            return gameboards, exit_criteria, periodicity, i
    return gameboards, 'survival', 0, i

def check_exit_criteria(gameboards):
    length = len(gameboards)
    last_gameboard = gameboards[length-1]
    previous_gameboard = gameboards[length-2]
    previous_gameboards = gameboards[0:(length-1)]
    

    # check if extinct (all empty)

    if np.sum(last_gameboard[0]) == 0:
        return "extinct", 0


    # check if equals

    if gameboard_equal(last_gameboard, previous_gameboard, True):
        return "stable", 0
    
    # check if oscillator
    osc_check, periodicity = check_exists(last_gameboard, previous_gameboards, True)
    if osc_check:
        return "oscillator", periodicity

    # check if spaceship
    spaceship_check, periodicity = check_exists(last_gameboard, previous_gameboards, False)
    if spaceship_check:
        return "spaceship", periodicity

    # else
    return 'survival', 0

def check_exists(gameboard_to_check, gameboards, check_origin):
    length = len(gameboards)
    
    for i in range(length-1, 0, -1):
        gameboard_to_compare = gameboards[i]
        res = gameboard_equal(gameboard_to_check, gameboard_to_compare, check_origin)
        if res: return True, length - i
    return False, -1





    #counter = sum(1 if x==y else -1 for x, y in product (last_gameboard, i))


def convert_to_string(gameboard):
    
    gb_array = gameboard[0].ravel()

    gb_bits = gb_array.astype(int)

    # gb_int = bits_to_int(gb_bits)

    gb_str = ''.join(map(str, gb_bits))
    gb_int = int(gb_str, 2)
    gb_hex = hex(gb_int)
    # IDEA: base64 would be even more efficient than hex.
    # gb_64 = base64.b64encode(gb_bits)

    width = len(gameboard[0][0])
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
    input_array = gb_array_2D.astype(bool)

    gameboard = gm.create_gameboard(input_array)

    return gameboard


#generate csv file


def generate_simulation(rows,cols,max_runs):
    cells = rows * cols
    max_value = (2**cells)-1

    results_header = ['start_gameboard', 'end_gameboard', 'exit_criteria', 'periodicity', 'rows', 'cols', 'max_height', 'max_width', 'runs']

    with open(f'simulation_results_{rows}_{cols}.csv', 'w',  newline='') as file:
        writer = csv.writer(file)
        writer.writerow(results_header)

        gameboard_sim_start_history = []

        simulation_count = 0


        max_max_runs = max_p = max_max_height = max_max_width = 0

        start = dt.datetime.now()

        for gameboard_int in range(max_value):

            gb_bin = bin(gameboard_int)[2:]
            gb_bin = gb_bin.zfill(cells)
            gb_array_1D = np.fromstring(gb_bin,'u1') - ord('0')
            gb_array_2D = np.reshape(gb_array_1D, (rows, cols))
            gameboard = gm.Gameboard(gb_array_2D.astype(bool))

            gameboard = gam.cut_both_axis(gameboard)
            
            if gameboard_int > 0 and  gameboard_int % 1000 == 0:
                dt_diff = dt.datetime.now() - start
                prog = gameboard_int/max_value
                expected_end = dt.datetime.now() + dt_diff * (1.0 - prog) / prog
                print(f'{simulation_count} simulations for {gameboard_int}/{max_value} gameboards. Max p/h/w/r: {max_p}/{max_max_width}/{max_max_height}/{max_max_runs} Progress: {int(100*prog)}%. Expected end: {expected_end}')

            if gameboard.shape != (rows, cols):
                #skipping non-full 
                continue
            

            # check if current gb is in history
            # NOTE: debug only
            already_simulated = check_similar_exists(gameboard_sim_start_history, gameboard)

            if already_simulated:
              continue              

            gameboards, exit_criteria, periodicity, runs = run_simulation(gameboard, max_runs)
           

            start_gameboard = convert_to_string(gameboard)
            end_gameboard = convert_to_string(gameboards[len(gameboards)-1])

            max_height= np.shape(gameboards[len(gameboards)-1])[0]
            max_width = np.shape(gameboards[len(gameboards)-1])[1]

            max_max_runs = max(max_max_runs, runs)
            max_p = max(max_p, periodicity)
            max_max_height = max(max_max_height, max_height)
            max_max_width = max(max_max_width, max_width)

            new_row = [start_gameboard, end_gameboard, exit_criteria, periodicity, rows, cols, max_height, max_width, runs]

            writer.writerow(new_row)

            simulation_count += 1

def check_similar_exists(gameboard_sim_start_history, gameboard):
    exists = False
    cut_gb = gam.cut_both_axis(gameboard)
    for past_gameboard in gameboard_sim_start_history:
        exists = gameboard_equal(cut_gb,past_gameboard)
        if exists:
            break
    
    if not exists:
        gameboard_sim_start_history.append(cut_gb)
    
    return exists

        
    
def main():
    generate_simulation(3,3,100)

if __name__ == "__main__":
    main()
