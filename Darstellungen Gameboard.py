import basic_game_functions as bgf


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