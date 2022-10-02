import basic_game_functions as gamefun

def get_gleiter(size = 8):
    gameboard = gamefun.create_gameboard(rows = size, cols = size)
    gameboard[4,1] = True
    gameboard[4,2] = True
    gameboard[4,3] = True
    gameboard[3,3] = True
    gameboard[2,2] = True
    return gameboard



# TODO: viele weitere Beispiele einfügen!