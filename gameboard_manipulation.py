import numpy as np

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
