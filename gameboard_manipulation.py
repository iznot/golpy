
import numpy as np
import basic_game_functions as gm



def cut_both_axis(gb):
    gb1 = cut(gb, 0)
    gb2 = cut(gb1, 1)
    return gb2

def cut(gb, axis = 0):
    gb = gb.copy()
    #überflüssige cols herausfinden
    sums = np.sum(gb, axis = axis)

    idx = np.where(sums != 0)[0]

    if len(idx) == 0:
        idx = [0]

    min = idx[0]
    max = idx[-1]
    sums[min:max+1] = 1
    
    if axis == 0:
        gb = gb[:,sums == 1]
        gb.origin = (gb.origin[0], gb.origin[1] - min)
    else:
        gb = gb[sums == 1,]
        gb.origin = (gb.origin[0] - min, gb.origin[1])

    return gb



def expand_gameboard_if_necessary(gb):
    gb = gb.copy()
    gb = gm.Gameboard(gb, origin = gb.origin)
    if sum(gb[0, :]) > 0:
        #add first row
        gb = np.insert(gb, 0, 0, axis = 0)
        gb.origin = (gb.origin[0]+1, gb.origin[1])


    if sum(gb[:, 0]) > 0:
        #add first column
        gb = np.insert(gb, 0, 0, axis = 1)
        gb.origin = (gb.origin[0], gb.origin[1]+1)
    
    
    if sum(gb[:, gb.shape[1]-1]) > 0 :
        gb = np.insert(gb, gb.shape[1], 0, axis = 1)
    
    if sum(gb[gb.shape[0]-1, :]) > 0 :
        gb = np.insert(gb, gb.shape[0], 0, axis = 0)
    return gb
