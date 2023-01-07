import os

import numpy as np
from scipy.ndimage import convolve

"""Dieses File stellt die grundlegenden Funktionen zu Verfügung, mit denen man Conway's Game of Life spielen kann. Es definiert das Grundobjekt (Konfiguration), die Ausgabe, sowie die Spielzüge.
"""

def create_configuration(input_array = None, rows = None, cols = None, origin=(0,0)):
    """Erstellt eine Konfiguration.

    Args:
        input_array (numpy.array, optional): Der 2-dimensionale Array bestehend aus boolean, wobei True die lebenden Zellen beschreibt. Ist dieser None, so wird eine leere Konfiguration erstellt.
        rows (int, optional): Die Anzahl Zeilen. Das hat nur einen Einfluss falls input_array = None.
        cols (_type_, optional): Die Anzahl Spalten. Das hat nur einen Einfluss falls input_array = None.
        origin (tuple, optional): Die Position relativ zum Ursprung auf dem Gameboard. Default = (0,0).

    Returns:
        Tuple: Der erste Wert im Tupel ist der numpy.array mit toten und lebenden Zellen. Der zweite Wert ist die relative Position zum Ursprung.
    """    
    if input_array is None:
        input_array = np.full((rows,cols), False)
    return (input_array, origin)


def print_gameboard(configuration):
    """Gibt das Gameboard in die Konsole aus.

    Args:
        configuration (Tuple): Die Konfiguration.
    """
    txt = get_gameboard_text(configuration)
    print(txt)

def get_gameboard_text(configuration, horizontal_separator : bool = True) -> str:
    """Generiert einen text string von einem Gameboard

    Args:
        configuration: Die Konfiguration
    """
    rows = configuration[0].shape[0]
    cols = configuration[0].shape[1]
    
    
    sep_line = ' ---' * cols + ' '
    
    if horizontal_separator:
        res = sep_line +  os.linesep
    else:
        res = ''

    for row in range(rows):
        
        second_line = '|'
        for col in range(cols):
            # Zelle:
            # 1. Zelle in gameboard abfragen
            cell_value = configuration[0][row, col]
            # 2. wenn false, dann '   |'
            if cell_value == False:
                cell_string = '   |'
            # 3. sonst: ' o |'
            else:
                cell_string = ' o |'
            # 4. Zelle zu second_line hinzufügen
            second_line += cell_string
        # second_line ausgeben
        
        res = res + second_line + os.linesep
        if horizontal_separator:
            res = res + sep_line + os.linesep

    
    res = res[:-1]
    
    return res


def get_neighbour_count(configuration):
    """Zählt die Anzahl Nachbarn jeder Zelle, wobei Randzellen "gewrappt" werden.

    Args:
        configuration: Die Konfiguration

    Returns:
        numpy.array(int): Ein zwei-dimensionaler Array, mit dim = Dimension des Gameboards.
    """    
    kernel = [[1, 1, 1],
              [1, 0, 1],
              [1, 1, 1]]

    nc = convolve(configuration[0].astype('int'), kernel, mode = 'wrap')
    return nc

def play(configuration):
    """Führt einen Spielzug durch.

    Args:
        configuration: Die Konfiguration

    Returns:
        configuration: Eine Konfiguration, die der nächsten Generation entspricht.
    """    
    neighbor_count = get_neighbour_count(configuration)

    get_alive = np.logical_and(configuration[0] == False, neighbor_count == 3)
    stay_alive = np.logical_and(configuration[0] == True, np.logical_or(neighbor_count == 2, neighbor_count == 3))

    gb_a = np.logical_or(get_alive, stay_alive)

    gb = (gb_a, configuration[1])
    return gb



def configuration_equal(configuration_1, configuration_2, check_origin: bool = True):
    """Überprüft, ob zwei Konfigurationen identisch sind.

    Args:
        configuration_1: Die erste Konfiguration
        configuration_2: Die zweite Konfiguration
        check_origin (bool, optional): Wenn True (Default), dann wird die relative Position zum Ursprung ebenfalls geprüft.

    Returns:
        bool: True wenn die Konfigurationen identisch sind.
    """    
    if configuration_1[0].shape != configuration_2[0].shape:
        return False
    if check_origin and configuration_1[1] != configuration_2[1]:
        return False
    result = np.array_equal(configuration_1[0], configuration_2[0])
    return result