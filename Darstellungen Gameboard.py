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
gb1 = bgf.create_gameboard(5,5)
gb1[0,0] = True
gb1[0,4] = True
gb1[4,4] = True
gb1[4,0] = True
bgf.print_gameboard(gb1)