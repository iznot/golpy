import csv
import datetime as dt
import itertools as ito
import os

import numpy as np
from joblib import Parallel, delayed

import basic_game_functions as gm
import gameboard_manipulation as gam


def run_simulation(gameboard, max_runs):
    
    gameboards = [gameboard]
    for i in range(1, max_runs):
        #NOTE: notwendig vorher, falls Anfangsposition am Rand
        gameboard = gam.expand_gameboard_if_necessary(gameboard)
        gameboard = gm.play(gameboard)
        gameboard = gam.get_base_configuration(gameboard)
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

    if gm.configuration_equal(last_gameboard, previous_gameboard, True):
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
        res = gm.configuration_equal(gameboard_to_check, gameboard_to_compare, check_origin)
        if res: return True, length - i
    return False, -1





    #counter = sum(1 if x==y else -1 for x, y in product (last_gameboard, i))






#generate csv file

def generate_simulation(shape, alive_count, max_runs, folder = "sim", debug = False):
    if alive_count == 1 and not (shape[0] == shape[1] == 1):
        return
    cells = shape[0] * shape[1]
    max_value = (2**cells)

    results_header = ['start_gameboard', 'alive_count', 'end_gameboard', 'exit_criteria', 'periodicity', 'rows', 'cols', 'max_height', 'max_width', 'runs']


    file_name = f'{folder}/simulation_results_{shape[0]}_{shape[1]}_{alive_count}.csv'

    folder_exists = os.path.exists(folder)

    if not folder_exists:
        os.makedirs(folder)
    

    with open(file_name, 'w',  newline='') as file:
        writer = csv.writer(file)
        writer.writerow(results_header)

        gb_already_checked_set = set()

        simulation_count = 0


        max_max_runs = max_p = max_max_height = max_max_width = 0

        start = dt.datetime.now()

        modu = int(max_value / min(100, max_value))
        for gameboard_int in range(max_value if not debug else 1000):

            if gameboard_int > 0 and  gameboard_int % modu == 0:
                dt_diff = dt.datetime.now() - start
                prog = gameboard_int/max_value
                expected_end = dt.datetime.now() + dt_diff * (1.0 - prog) / prog
                print(f'Shape {shape[0]}x{shape[1]} alive: {alive_count} {simulation_count} simulations for {gameboard_int}/{max_value} gameboards. Max p/h/w/r: {max_p}/{max_max_width}/{max_max_height}/{max_max_runs} Progress: {int(100*prog)}%. Expected end: {expected_end}')

            
            if gameboard_int in gb_already_checked_set:
                continue

            gb_bin = bin(gameboard_int)[2:]
            gb_bin = gb_bin.zfill(cells)
            gb_array_1D = np.fromstring(gb_bin,'u1') - ord('0')

            if not np.sum(gb_array_1D) == alive_count:
                continue

            
            gb_array_2D = np.reshape(gb_array_1D, (shape[0], shape[1]))
            gameboard = gm.create_configuration(gb_array_2D.astype(bool))

            gameboard = gam.get_base_configuration(gameboard)
            
            if not (gameboard[0].shape[0] == shape[0] and gameboard[0].shape[1] == shape[1]):
                #skipping non-full
                continue
            
            
            # check if current gb is in history
            add_gb_variations(gameboard, gb_already_checked_set)

            
            gameboards, exit_criteria, periodicity, runs = run_simulation(gameboard, max_runs)
           

            start_gameboard = gam.convert_to_string_representation(gameboard)
            end_gameboard = gam.convert_to_string_representation(gameboards[len(gameboards)-1])

            # TODO: überprüfen, sieht komisch aus
            max_height= np.shape(gameboards[len(gameboards)-1][0])[0]
            max_width = np.shape(gameboards[len(gameboards)-1][0])[1]

            max_max_runs = max(max_max_runs, runs)
            max_p = max(max_p, periodicity)
            max_max_height = max(max_max_height, max_height)
            max_max_width = max(max_max_width, max_width)

            new_row = [start_gameboard, alive_count, end_gameboard, exit_criteria, periodicity, shape[0], shape[1], max_max_height, max_max_width, runs]

            writer.writerow(new_row)

            simulation_count += 1

def add_gb_variations(gb, gb_already_checked_set):

    gb_variation_set = gam.get_configuration_variations(gb)

    gb_already_checked_set.update(gb_variation_set)
    

    
    
def simulation_for_generations(rows, cols, max_runs):
    cells = rows*cols
    max_value = 2^(cells)
    cut_gameboards = []
    generations_header = ['Startkonfiguration']

    for i in max_runs[2:]:
        i = 'Generation' + i
        generations_header.append(i)
        

    with open(f'generations_of_gameboards', 'w',  newline='') as file:
        writer = csv.writer(file)
        writer.writerow(generations_header)


    for gameboard_int in range(max_value):
        gb_bin = bin(gameboard_int)[2:]
        gb_bin = gb_bin.zfill(cells)
        gb_array_1D = np.fromstring(gb_bin,'u1') - ord('0')
        gb_array_2D = np.reshape(gb_array_1D, (rows, cols))
        gameboard = gm.create_configuration(gb_array_2D.astype(bool))
        gameboard = gam.get_base_configuration(gameboard)

        gameboards, exit_criteria, periodicity, runs = run_simulation(gameboard, 2)

        for gb in gameboards:
            gameboard = gam.get_base_configuration(gb)
            cut_gameboards.append(gameboard)

        new_row = cut_gameboards
        writer.writerow(new_row)

        
def get_dimensions(i, j):
    list1 = list(range(1, i + 1))
    list2 = list(range(1, j + 1))
    
    lp = ito.product(list1, list2)
    lpl = list(lp)
    for n in range(len(lpl)-1, 0, -1):
        if lpl[n][0] > lpl[n][1]:
            del lpl[n]


    lpl.reverse()
    return lpl


def main():
    
    #dims = get_dimensions(5, 5)
    
    dims = [(5,6)]

    def process(dim, alive_count):
        generate_simulation(dim , alive_count, 100, debug=False)
    
    Parallel(n_jobs=8)(delayed(process)(dim, alive_count) for dim in dims for alive_count in range(1, dim[0]*dim[1] + 1))

    #for dim in dims: process(dim)
    

    

if __name__ == "__main__":
    main()

    
