
import numpy as np
import basic_game_functions as gm



def cut_both_axis(gb):
    gb1 = cut(gb, 0)
    gb2 = cut(gb1, 1)
    return gb2

def cut(gb, axis = 0):
    
    #überflüssige cols herausfinden
    sums = np.sum(gb[0], axis = axis)

    idx = np.where(sums != 0)[0]

    if len(idx) == 0:
        idx = [0]

    min = idx[0]
    max = idx[-1]
    sums[min:max+1] = 1
    
    if axis == 0:
        gb = (gb[0][:,sums == 1], (gb[1][0], gb[1][1] - min))
    else:
        gb = (gb[0][sums == 1,], (gb[1][0] - min, gb[1][1]))

    return gb



def expand_gameboard_if_necessary(gb):
    if sum(gb[0][0, :]) > 0:
        #add first row
        gb = (np.insert(gb[0], 0, 0, axis = 0), (gb[1][0]+1, gb[1][1]))


    if sum(gb[0][:, 0]) > 0:
        #add first column
        gb = (np.insert(gb[0], 0, 0, axis = 1), (gb[1][0], gb[1][1]+1))
    
    if sum(gb[0][:, gb[0].shape[1]-1]) > 0 :
        gb = (np.insert(gb[0], gb[0].shape[1], 0, axis = 1), gb[1])
    
    if sum(gb[0][gb[0].shape[0]-1, :]) > 0 :
        gb = (np.insert(gb[0], gb[0].shape[0], 0, axis = 0), gb[1])
    return gb


def get_gameboard_variations(gb):
    """Gibt eine Liste von allen unterschiedlichen "ähnlichen" Gameboards.
    D.h. gespiegelt und gedreht.

    Args:
        gb (_type_): Das Gameboard, für welches wir die Variationen suchen.

    Returns:
        _type_: _description_
    """    
    quadratic = gb[0].shape[0] == gb[0].shape[1]

    
    gb_rota_1 = np.rot90(gb[0])
    gb_rota_2 = np.rot90(gb_rota_1)
    
    
    gb_reflected = np.flip(gb[0], axis = 0)
    gb_reflected_rota_1 = np.rot90(gb_reflected)
    gb_reflected_rota_2 = np.rot90(gb_reflected_rota_1)
    

    if quadratic:
        
        gb_rota_3 = np.rot90(gb_rota_2)
        gb_reflected_rota_3 = np.rot90(gb_reflected_rota_2)

        gb_variations_number_set = {get_gb_nbr(gb[0]),
                        get_gb_nbr(gb_rota_1), 
                        get_gb_nbr(gb_rota_2), 
                        get_gb_nbr(gb_rota_3), 
                        get_gb_nbr(gb_reflected),
                        get_gb_nbr(gb_reflected_rota_1), 
                        get_gb_nbr(gb_reflected_rota_2), 
                        get_gb_nbr(gb_reflected_rota_3)}

    else:
        gb_variations_number_set = {get_gb_nbr(gb[0]), 
                        get_gb_nbr(gb_rota_2),
                        get_gb_nbr(gb_reflected),
                        get_gb_nbr(gb_reflected_rota_2)}

    return gb_variations_number_set
    
def get_gb_nbr(gb):
    
    gb_array = gb.ravel()
    gb_bits = gb_array.astype(int)

    # gb_int = bits_to_int(gb_bits)

    gb_str = ''.join(map(str, gb_bits))
    gb_int = int(gb_str, 2)

    return gb_int
