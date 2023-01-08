import csv
import datetime as dt
import itertools as ito
import os

import numpy as np
from joblib import Parallel, delayed

import game
import gameboard_manipulation as gam
import play

#generate csv file

def generate_simulation(gameboard_shape, alive_count, max_runs, folder = "sim", debug = False):
    """Läuft eine Simulation durch

    Args:
        gameboard_shape (tuple): Die Dimensionen des Gameboards
        alive_count (int): Die Anzahl lebender Zellen
        max_runs (int): Die maximale Anzahl Spielzüge, bis ein Spiel abbricht
        folder (str, optional): Der Folder, in welchen die Resultate geschrieben werden. 
        debug (bool, optional): Falls True, werden maximal 1000 Konfigurationen simuliert.
    """    
    if alive_count == 1 and not (gameboard_shape[0] == gameboard_shape[1] == 1):
        return
    cells = gameboard_shape[0] * gameboard_shape[1]
    max_value = (2**cells)

    results_header = ['start_gameboard', 'alive_count', 'end_gameboard', 'exit_criteria', 'periodicity', 'rows', 'cols', 'max_height', 'max_width', 'runs']


    file_name = f'{folder}/simulation_results_{gameboard_shape[0]}_{gameboard_shape[1]}_{alive_count}.csv'

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
        for config_int in range(max_value if not debug else 1000):

            if config_int > 0 and  config_int % modu == 0:
                dt_diff = dt.datetime.now() - start
                prog = config_int/max_value
                expected_end = dt.datetime.now() + dt_diff * (1.0 - prog) / prog
                print(f'Shape {gameboard_shape[0]}x{gameboard_shape[1]} alive: {alive_count} {simulation_count} simulations for {config_int}/{max_value} gameboards. Max p/h/w/r: {max_p}/{max_max_width}/{max_max_height}/{max_max_runs} Progress: {int(100*prog)}%. Expected end: {expected_end}')

            
            if config_int in gb_already_checked_set:
                continue

            config_bin = bin(config_int)[2:]
            config_bin = config_bin.zfill(cells)
            config_array_1D = np.fromstring(config_bin,'u1') - ord('0')

            if not np.sum(config_array_1D) == alive_count:
                continue

            
            config_array_2D = np.reshape(config_array_1D, (gameboard_shape[0], gameboard_shape[1]))
            configuration = play.create_configuration(config_array_2D.astype(bool))

            configuration = gam.get_base_configuration(configuration)
            
            if not (configuration[0].shape[0] == gameboard_shape[0] and configuration[0].shape[1] == gameboard_shape[1]):
                #skipping non-full
                continue
            
            
            # check if current gb is in history
            _add_config_variations(configuration, gb_already_checked_set)

            
            generations, exit_criteria, periodicity, runs = game.play_full_game(configuration, max_runs)
           

            start_configuration = gam.convert_to_string_representation(configuration)
            end_configuration = gam.convert_to_string_representation(generations[len(generations)-1])

            # TODO: überprüfen, sieht komisch aus
            max_height= np.shape(generations[len(generations)-1][0])[0]
            max_width = np.shape(generations[len(generations)-1][0])[1]

            max_max_runs = max(max_max_runs, runs)
            max_p = max(max_p, periodicity)
            max_max_height = max(max_max_height, max_height)
            max_max_width = max(max_max_width, max_width)

            new_row = [start_configuration, alive_count, end_configuration, exit_criteria, periodicity, gameboard_shape[0], gameboard_shape[1], max_max_height, max_max_width, runs]

            writer.writerow(new_row)

            simulation_count += 1

def _add_config_variations(configuration, configuration_already_checked_set):

    gb_variation_set = gam.get_configuration_variations(configuration)

    configuration_already_checked_set.update(gb_variation_set)
    


def main():
    """Startet eine Simulation.
    """    
    
    #dims = get_dimensions(5, 5)
    
    dims = [(5,6)]

    def process(dim, alive_count):
        generate_simulation(dim , alive_count, 100, debug=False)
    
    Parallel(n_jobs=8)(delayed(process)(dim, alive_count) for dim in dims for alive_count in range(1, dim[0]*dim[1] + 1))

    #for dim in dims: process(dim)
    

    

if __name__ == "__main__":
    main()

    
