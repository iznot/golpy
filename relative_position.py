from re import M
import numpy as np
import basic_game_functions as bgf
import samples as sam

gb = sam.get_gleiter()
rows, cols = gb.shape
two_d = gb.ravel()
first_true = np.where(two_d == True)[0][0]
two_d = np.roll(two_d, -first_true)
gb = np.reshape(two_d, (rows, cols))
bgf.print_gameboard(gb)

#leere enden unten und rechts abschneiden, für unten umgekehrtes von vorher, für rechts matrix umdrehen (transpose) 
