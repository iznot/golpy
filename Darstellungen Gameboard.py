import basic_game_functions as bgf
import numpy as np


#NOTE Beispiels Gameboard
gb = bgf.create_gameboard(5,5)
gb[2,1] = True
gb[3,2] = True
gb[4,0] = True
bgf.print_gameboard(gb)
gb = bgf.play(gb)
bgf.print_gameboard(gb)



#NOTE Grenzfälle
gb1 = bgf.create_gameboard(7,7)
gb1[1,1] = True
gb1[1,5] = True
gb1[5,5] = True
gb1[5,1] = True
bgf.print_gameboard(gb1)
gb1 = bgf.play(gb1)
bgf.print_gameboard(gb1)

#NOTE Gameboard als Zahl
gb1 = bgf.create_gameboard(5,5)
gb1[3,2] = True
gb1[1,4] = True
gb1[3,3] = True
gb1[2,4] = True
bgf.print_gameboard(gb1)


#NOTE Dezimalzahl als Gameboard
bin = '1'
cells = 5*5
rows = cols = 5
gb_bin=bin.zfill(cells)
gb_array_1D = np.fromstring(gb_bin,'u1') - ord('0')
gb_array_2D = np.reshape(gb_array_1D, (rows, cols))
gameboard = bgf.Gameboard(gb_array_2D.astype(bool))
print(gameboard)


#NOTE Beispiel Lebensentwicklung
gb1 = bgf.create_gameboard(5,5)
gb1[1,1] = True
gb1[1,2] = True
gb1[2,1] = True
gb1[3,2] = True
bgf.print_gameboard(gb1)
gb1 = bgf.play(gb1)
bgf.print_gameboard(gb1)
gb1 = bgf.play(gb1)
bgf.print_gameboard(gb1)
gb1 = bgf.play(gb1)
bgf.print_gameboard(gb1)

