import numpy as np
from itertools import product
import gameboard_manipulation as gam
import basic_game_functions as gm

import csv
import datetime as dt
import operator
from ast import literal_eval


def run_simulation(gameboard, max_runs):
    
    gameboards = [gameboard]
    for i in range(1, max_runs):
        #NOTE: notwendig vorher, falls Anfangsposition am Rand
        gameboard = gam.expand_gameboard_if_necessary(gameboard)
        gameboard = gm.play(gameboard)
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

    if gm.gameboard_equal(last_gameboard, previous_gameboard, True):
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
        res = gm.gameboard_equal(gameboard_to_check, gameboard_to_compare, check_origin)
        if res: return True, length - i
    return False, -1





    #counter = sum(1 if x==y else -1 for x, y in product (last_gameboard, i))


def convert_to_string(gameboard):
    
    gameboard_cut = gam.cut_both_axis(gameboard)

    gb_array = gameboard_cut[0].ravel()

    gb_bits = gb_array.astype(int)

    # gb_int = bits_to_int(gb_bits)

    gb_str = ''.join(map(str, gb_bits))
    gb_int = int(gb_str, 2)
    gb_hex = hex(gb_int)
    # IDEA: base64 would be even more efficient than hex.
    # gb_64 = base64.b64encode(gb_bits)

    shape = gameboard[0].shape
    shape_cut = gameboard_cut[0].shape
    leading_zeroes= get_leading_zeroes(gb_bits)
    origin = tuple(map(lambda x, y: -(x - y), gameboard_cut[1], gameboard[1]))
    res = f'{shape}:{origin}|{shape_cut}:{leading_zeroes}:{gb_hex}'
    return res


def get_leading_zeroes(bits):
    i = np.argmax(bits!=0)
    if i==0 and np.all(bits==0): i=len(bits)
    return i

def convert_to_gameboard(gameboard_str):
    res_list = gameboard_str.split('|')
    gb_specs = res_list[0].split(':')
    set_specs = res_list[1].split(':')

    
    
    shape = literal_eval(set_specs[0])
    leading_zeroes = int(set_specs[1])
    gb_hex_str = set_specs[2]

    gb_int = int(gb_hex_str, 16)
    gb_bin = bin(gb_int)[2:]
    gb_bin = gb_bin.zfill(len(gb_bin) + leading_zeroes)
    gb_array_1D = np.fromstring(gb_bin,'u1') - ord('0')
    gb_array_2D = np.reshape(gb_array_1D, shape)
    input_array = gb_array_2D.astype(bool)

    gameboard = gm.create_gameboard(input_array)


    # fit into large
    full_shape = literal_eval(gb_specs[0])
    origin = literal_eval(gb_specs[1])

    full_gameboard_a = np.full(full_shape, False)

    full_gameboard_a[ origin[0]:(origin[0]+shape[0])  , origin[1]:(origin[1]+shape[1])   ] = gameboard[0]
#TODO wieso brauchts diese komische Form und 'full_gameboard_a' reicht nicht aus?
    gameboard = gm.create_gameboard(full_gameboard_a)


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
            gameboard = gm.create_gameboard(gb_array_2D.astype(bool))

            gameboard = gam.cut_both_axis(gameboard)
            
            if gameboard_int > 0 and  gameboard_int % 1000 == 0:
                dt_diff = dt.datetime.now() - start
                prog = gameboard_int/max_value
                expected_end = dt.datetime.now() + dt_diff * (1.0 - prog) / prog
                print(f'{simulation_count} simulations for {gameboard_int}/{max_value} gameboards. Max p/h/w/r: {max_p}/{max_max_width}/{max_max_height}/{max_max_runs} Progress: {int(100*prog)}%. Expected end: {expected_end}')

            if gameboard[0].shape != (rows, cols):
                #skipping non-full 
                continue
            

            # check if current gb is in history
            # NOTE: debug only
            already_simulated = compare_rotated(gameboard_sim_start_history, gameboard)

            if already_simulated:
              continue              

            gameboards, exit_criteria, periodicity, runs = run_simulation(gameboard, max_runs)
           

            start_gameboard = convert_to_string(gameboard)
            end_gameboard = convert_to_string(gameboards[len(gameboards)-1])

            max_height= np.shape(gameboards[len(gameboards)-1][0])[0]
            max_width = np.shape(gameboards[len(gameboards)-1][0])[1]

            max_max_runs = max(max_max_runs, runs)
            max_p = max(max_p, periodicity)
            max_max_height = max(max_max_height, max_height)
            max_max_width = max(max_max_width, max_width)

            new_row = [start_gameboard, end_gameboard, exit_criteria, periodicity, rows, cols, max_height, max_width, runs]

            writer.writerow(new_row)

            simulation_count += 1

def check_similar_exists(gameboard_sim_start_history, gb, gb1, gb2, gb3):
    exists = False
    for past_gameboard in gameboard_sim_start_history:
        exists = gm.gameboard_equal(gb,past_gameboard)
        if exists:
            break
    for past_gameboard in gameboard_sim_start_history:
        exists = gm.gameboard_equal(gb1,past_gameboard)
        if exists:
            break
    for past_gameboard in gameboard_sim_start_history:
        exists = gm.gameboard_equal(gb2,past_gameboard)
        if exists:
            break
    for past_gameboard in gameboard_sim_start_history:
        exists = gm.gameboard_equal(gb3,past_gameboard)
        if exists:
            break
    
    if not exists:
        gameboard_sim_start_history.append(gb)
    
    return exists

        
    
def main():
    generate_simulation(4,4,100)

if __name__ == "__main__":
    main()

def compare_rotated(gameboard_sim_start_history, gb):
    cut_gb = gam.cut_both_axis(gb)
    cut_1, cut_2, cut_3 = gam.turn_gb(gb)
    exists = check_similar_exists(gameboard_sim_start_history, cut_gb, cut_1, cut_2, cut_3)
    return exists

