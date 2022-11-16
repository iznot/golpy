from operator import itemgetter
from re import M
import numpy as np
import basic_game_functions as bgf
import samples as sam


#Axis = 0 = cols, Axis = 1 = rows

gb = sam.get_gleiter(6)
bgf.print_gameboard(gb)

#überflüssige cols herausfinden & abcutten
col_sums = np.sum(gb, axis = 0)
left_col_has_alive = list(map(lambda x: bool(min(x, 1)), col_sums))
left_cut = np.where(left_col_has_alive)[0][0]

gb = np.delete(gb,np.s_[0:left_cut], 1)
#überflüssige rows herausfinden & abcutten
row_sums = np.sum(gb, axis = 1)
upper_row_has_alive = list(map(lambda x: bool(min(x, 1)), row_sums))
upper_cut = np.where(upper_row_has_alive)[0][0]

gb = np.delete(gb, np.s_[0:upper_cut], 0)
#gb = gb[row_has_alive, col_has_alive]

#Um 180° Drehen 
gb = np.rot90(gb,2)

#Noch mal das selbe für jetztige cols
col_sums = np.sum(gb, axis = 0)
right_col_has_alive = list(map(lambda x: bool(min(x, 1)), col_sums))
right_cut = np.where(right_col_has_alive)[0][0]

gb = np.delete(gb,np.s_[0:right_cut], 1)

#Noch mal das selbe für jetztige rows
row_sums = np.sum(gb, axis = 1)
bottom_row_has_alive = list(map(lambda x: bool(min(x, 1)), row_sums))
bottom_cut = np.where(bottom_row_has_alive)[0][0]

gb = np.delete(gb,np.s_[0:bottom_cut], 1)
