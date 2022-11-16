from re import M
import numpy as np

import basic_game_functions as bgf

# die erste Zahl gibt die Anzahl Zeilen (y-Achse, rows), die zweite Zahl die Anzahl Spalten (x-Achse, cols)

x = np.full((9,9), False)

x[3,4] = True
x[4,3] = True
x[7,2] = True

print(x)

bgf.print_gameboard(x)

x2 = bgf.play(x)
print('x2:')
bgf.print_gameboard(x2)



