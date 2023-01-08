import numpy as np

import play
import manipulation as gam


def play_full_game(start_configuration, max_runs):
    """Spielt ein Spiel.

    Args:
        start_configuration: Die Anfangskonfiguration
        max_runs (int): Die maximale Anzahl Spielzüge.

    Returns:
        generations: Eine Liste aller Generationen.
        exit_criteria (str): Die Spielklasse dieses Spiels, also 'survival', 'extinct', 'stable', 'oscillator', 'spaceship'
        periodicity (int): Die Periodizität des Objekts falls exit_criteria = 'oscillator' | 'spaceship'. Sonst 0.
        i (int): Die Anzahl Spielzüge bis zum Erkennen des exit_criteria (oder max_runs).
    """    
    generations = [start_configuration]
    for i in range(1, max_runs):
        start_configuration = gam.expand_gameboard_if_necessary(start_configuration)
        start_configuration = play.play(start_configuration)
        start_configuration = gam.get_base_configuration(start_configuration)
        generations.append(start_configuration)
        exit_criteria, periodicity = check_exit_criteria(generations)
        if exit_criteria != 'survival':
            return generations, exit_criteria, periodicity, i
    return generations, 'survival', 0, i

def check_exit_criteria(game):
    """Überprüft, ob ein Spiel einer Spielklasse zugeordnet werden kann.

    Args:
        game (list): Eine Liste mit allen bisherigen Generationen des Spiels.

    Returns:
        str: Die Spielklasse, falls identifiziert, oder 'survival'
    """    
    length = len(game)
    last_generation = game[length-1]
    previous_generation = game[length-2]
    previous_game = game[0:(length-1)]
    

    # check if extinct (all empty)

    if np.sum(last_generation[0]) == 0:
        return "extinct", 0


    # check if equals

    if gam.configuration_equal(last_generation, previous_generation, True):
        return "stable", 0
    
    # check if oscillator
    osc_check, periodicity = _check_exists(last_generation, previous_game, True)
    if osc_check:
        return "oscillator", periodicity

    # check if spaceship
    spaceship_check, periodicity = _check_exists(last_generation, previous_game, False)
    if spaceship_check:
        return "spaceship", periodicity

    # else
    return 'survival', 0

def _check_exists(configuration_to_check, game, check_origin):
    length = len(game)
    
    for i in range(length-1, 0, -1):
        gameboard_to_compare = game[i]
        res = gam.configuration_equal(configuration_to_check, gameboard_to_compare, check_origin)
        if res: return True, length - i
    return False, -1

