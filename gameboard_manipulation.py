
import numpy as np



def cut_both_axis(gb):
    gb1 = cut(gb, 0)
    gb2 = cut(gb1, 1)
    return gb2

def cut(gb, axis = 0):

    #überflüssige cols herausfinden
    sums = np.sum(gb, axis = axis)
    for i in range(0, len(sums)-1):
        if sums[i] == 0:
            sums[i] = -1
        else:
            sums[i] = 1
            break

    for i in range(len(sums)-1, 0, -1):
        if sums[i] == 0:
            sums[i] = -1
        else:
            sums[i] = 1
            break
    
    sums[sums == 0] = 1
    sums[sums == -1] = 0
 
    #abcutten
    if axis == 0:
        gb_cut = gb[:,sums == 1]
    else:
        gb_cut = gb[sums == 1,:]

    return gb_cut


def expand_gameboard(gb):
    rows = gb.shape[0]
    cols = gb.shape[1]
    if sum(gb[:, 0]) > 0:
        #add first colum
        gb = np.insert(gb, 0, 0, axis = 1)
    
    if sum(gb[0, :]) > 0:
        #add first row
        gb = np.insert(gb, 0, 0, axis = 0)
    
    if sum(gb[:, cols]) > 0 :
        gb = np.insert(gb, cols + 1, 0, axis = 1)
    
    if sum(gb[rows, :]) > 0 :
        gb = np.insert(gb, rows + 1, 0, axis = 0)
    #TODO: add other axis
    return gb