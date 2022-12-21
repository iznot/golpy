
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


def turn_gb(gb):
    gb1 = gm.create_gameboard(np.rot90(gb[0]))
    gb2 = gm.create_gameboard(np.rot90(gb1[0]))
    gb3 = gm.create_gameboard(np.rot90(gb2[0]))
    gb4 = gm.create_gameboard(np.flip(gb[0], axis = 0))
    gb5 = gm.create_gameboard(np.flip(gb[0], axis = 1))

    return gb, gb1, gb2, gb3, gb4, gb5