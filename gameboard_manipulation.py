
import numpy as np
import basic_game_functions as gm



def cut_both_axis(gb):
    gb1 = try_cut_new(gb, 0)
    gb2 = try_cut_new(gb1, 1)
    return gb2

def cut(gb, axis = 0):

    #überflüssige cols herausfinden
    sums = np.sum(gb, axis = axis)
    for i in range(0, len(sums)-1):
        if sums[i] == 0:
            sums[i] = -1
        else:
            sums[i] 
            break

    for i in range(len(sums)-1, 0, -1):
        if sums[i] == 0:
            sums[i] = -1
        else:
            sums[i] 
            break
    
   # sums[sums == 0] = 1
    # sums[sums == -1] = 0
    

   


    gb_cut = []
    for i in sums:
        if i >= 0 :
            gb_cut.append(i)
    #abcutten
 #   if axis == 0:
  #      for i in sums:
   #         if i == -1:
    #            gb_cut = del i

   # else:
        #gb_cut = gb[sums == 1,:]

    return gb_cut


def expand_gameboard_if_necessary(gb):
    
    if sum(gb[:, 0]) > 0:
        #add first colum
        gb = np.insert(gb, 0, 0, axis = 1)
    
    if sum(gb[0, :]) > 0:
        #add first row
        gb = np.insert(gb, 0, 0, axis = 0)
    
    if sum(gb[:, gb.shape[1]-1]) > 0 :
        gb = np.insert(gb, gb.shape[1], 0, axis = 1)
    
    if sum(gb[gb.shape[0]-1, :]) > 0 :
        gb = np.insert(gb, gb.shape[0], 0, axis = 0)
    return gb

def try_cut_new(gb, axis = 0):
    sums = np.sum(gb, axis = axis)
    if axis == 0:
        other = 1
    else:
        other = 0
    for i in range(0, len(sums)-1):
        if sums[i] == 0:
            sums[i] = -1
        else:
            sums[i] 
            break
    
    cut_until = np.count_nonzero(sums == -1)
    gb_cut = np.delete(gb, np.s_[:cut_until], other)

    for i in range(len(sums)-1, 0, -1):
        if sums[i] == 0:
            sums[i] = -2
        else:
            sums[i] 
            break
    
    
    two = np.count_nonzero(sums ==-2) + 1
    length_sums = len(sums) 
    cut_from =length_sums - two
    gb_cut = np.delete(gb_cut, np.s_[cut_from:length_sums], other)
    return gb_cut

