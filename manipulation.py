from ast import literal_eval

import numpy as np

import play as play

"""Stellt Funktionen zur Verfügung, die benötigt werden um die Simulationen durchzuführen.
"""

def get_base_configuration(configuration):
    """Konvertiert eine Konfiguration zu ihrer Grundkonfiguration.

    Args:
        configuration: Die Konfiguration

    Returns:
        configuration: Die Grundkonfiguration
    """    
    config1 = _cut(configuration, 0)
    base_config = _cut(config1, 1)
    return base_config

def _cut(configuration, axis = 0):
    
    #überflüssige cols herausfinden
    sums = np.sum(configuration[0], axis = axis)

    idx = np.where(sums != 0)[0]

    if len(idx) == 0:
        idx = [0]

    min = idx[0]
    max = idx[-1]
    sums[min:max+1] = 1
    
    if axis == 0:
        configuration = (configuration[0][:,sums == 1], (configuration[1][0], configuration[1][1] - min))
    else:
        configuration = (configuration[0][sums == 1,], (configuration[1][0] - min, configuration[1][1]))

    return configuration



def expand_gameboard_if_necessary(configuration):
    """Erweitert ein Gameboard auf denjenigen Seiten, auf denen eine lebende Zelle am Rand ist.

    Args:
        configuration: Die allenfalls zu erweiterne Konfiguration

    Returns:
        configuration: die Konfiguration, die allenfalls erweitert wurde
    """    
    if sum(configuration[0][0, :]) > 0:
        #add first row
        configuration = (np.insert(configuration[0], 0, 0, axis = 0), (configuration[1][0]+1, configuration[1][1]))


    if sum(configuration[0][:, 0]) > 0:
        #add first column
        configuration = (np.insert(configuration[0], 0, 0, axis = 1), (configuration[1][0], configuration[1][1]+1))
    
    if sum(configuration[0][:, configuration[0].shape[1]-1]) > 0 :
        configuration = (np.insert(configuration[0], configuration[0].shape[1], 0, axis = 1), configuration[1])
    
    if sum(configuration[0][configuration[0].shape[0]-1, :]) > 0 :
        configuration = (np.insert(configuration[0], configuration[0].shape[0], 0, axis = 0), configuration[1])
    return configuration


def get_configuration_variations(configuration):
    """Gibt ein Set von allen affinen Grundkonfigurationen.
    D.h. gespiegelt und gedreht.

    Args:
        configuration: Die Konfiguration

    Returns:
        Set: Ein Set, das die Konfigurations-Zahlen der affinen Konfiguration enthält.
    """    
    quadratic = configuration[0].shape[0] == configuration[0].shape[1]

    
    config_rota_1 = np.rot90(configuration[0])
    config_rota_2 = np.rot90(config_rota_1)
    
    
    config_reflected = np.flip(configuration[0], axis = 0)
    config_reflected_rota_1 = np.rot90(config_reflected)
    config_reflected_rota_2 = np.rot90(config_reflected_rota_1)
    

    if quadratic:
        
        config_rota_3 = np.rot90(config_rota_2)
        config_reflected_rota_3 = np.rot90(config_reflected_rota_2)

        config_variations_number_set = {get_config_nbr(configuration[0]),
                        get_config_nbr(config_rota_1), 
                        get_config_nbr(config_rota_2), 
                        get_config_nbr(config_rota_3), 
                        get_config_nbr(config_reflected),
                        get_config_nbr(config_reflected_rota_1), 
                        get_config_nbr(config_reflected_rota_2), 
                        get_config_nbr(config_reflected_rota_3)}

    else:
        config_variations_number_set = {get_config_nbr(configuration[0]), 
                        get_config_nbr(config_rota_2),
                        get_config_nbr(config_reflected),
                        get_config_nbr(config_reflected_rota_2)}

    return config_variations_number_set
    
def get_config_nbr(configuration):
    """Transformiert eine Konfiguration in ihre dezimal-Räpresentation.

    Args:
        configuration: Die Konfiguration

    Returns:
        int: Eine Dezimalzahl, die der Konfiguration entspricht.
    """    
    
    config_array = configuration.ravel()
    config_bits = config_array.astype(int)
    config_str = ''.join(map(str, config_bits))
    config_int = int(config_str, 2)

    return config_int


def convert_to_string_representation(configuration):
    """Konvertiert eine Konfiguration in ihre Text-Repräsentation.

    Args:
        configuration: Die Konfiguration

    Returns:
        str: Die Konfiguration in ihrer String-Representation
    """    
    base_configuration, config_bits, config_int = convert_to_int(configuration)
    config_hex = hex(config_int)
    # IDEA: base64 would be even more efficient than hex.
    # gb_64 = base64.b64encode(gb_bits)

    shape = configuration[0].shape
    shape_cut = base_configuration[0].shape
    leading_zeroes= _get_leading_zeroes(config_bits)
    origin = tuple(map(lambda x, y: -(x - y), base_configuration[1], configuration[1]))
    res = f'{shape}:{origin}|{shape_cut}:{leading_zeroes}:{config_hex}'
    return res

def convert_to_int(configuration):
    base_configuration = get_base_configuration(configuration)

    config_array = base_configuration[0].ravel()

    config_bits = config_array.astype(int)

    config_str = ''.join(map(str, config_bits))
    config_int = int(config_str, 2)
    return base_configuration,config_bits,config_int


def _get_leading_zeroes(bits):
    i = np.argmax(bits!=0)
    if i==0 and np.all(bits==0): i=len(bits)
    return i

def create_configuration_from_string(configuration_str):
    """Konvertiert eine Text-Repräsentation in die dazugehörige Konfiguration.

    Args:
        str: Die Konfiguration in ihrer String-Representation
        
    Returns:
        configuration: Die Konfiguration
    """    
    res_list = configuration_str.split('|')
    config_specs = res_list[0].split(':')
    set_specs = res_list[1].split(':')

    
    
    shape = literal_eval(set_specs[0])
    leading_zeroes = int(set_specs[1])
    config_hex_str = set_specs[2]

    config_int = int(config_hex_str, 16)
    config_bin = bin(config_int)[2:]
    config_bin = config_bin.zfill(len(config_bin) + leading_zeroes)
    config_array_1D = np.fromstring(config_bin,'u1') - ord('0')
    config_array_2D = np.reshape(config_array_1D, shape)
    input_array = config_array_2D.astype(bool)

    config = play.create_configuration(input_array)


    # fit into large
    full_shape = literal_eval(config_specs[0])
    origin = literal_eval(config_specs[1])

    #NOTE: wir erstellen ein Gameboard mit der gewünschten Form (aber alles leer)
    full_gameboard_a = np.full(full_shape, False)

    #NOTE: jetzt platzieren wir die Figur an die richtige Stelle, relativ zum Ursprung
    full_gameboard_a[ origin[0]:(origin[0]+shape[0])  , origin[1]:(origin[1]+shape[1])   ] = config[0]

    config = play.create_configuration(full_gameboard_a)


    return config


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