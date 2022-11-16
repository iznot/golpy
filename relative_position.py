
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

    return(gb_cut)