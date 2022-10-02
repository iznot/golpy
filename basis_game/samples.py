import basic_game_functions as gamefun

def get_gleiter(size = 8):
    gameboard = gamefun.create_gameboard(rows = size, cols = size)
    gameboard[4,1] = True
    gameboard[4,2] = True
    gameboard[4,3] = True
    gameboard[3,3] = True
    gameboard[2,2] = True
    return gameboard

def get_erased(size = 50):
    gameboard = gamefun.create_gameboard(rows = size, cols = size)
    start_x = int(size / 2)
    gameboard[1,2] = True
    gameboard[1,3] = True
    gameboard[1,4] = True
    gameboard[2,2] = True
    gameboard[2,4] = True
    gameboard[3,2] = True
    gameboard[3,4] = True
    gameboard[5,2] = True
    gameboard[5,4] = True
    gameboard[6,2] = True
    gameboard[6,4] = True
    gameboard[7,2] = True
    gameboard[7,3] = True
    gameboard[7,4] = True
    return gameboard

# TODO: viele weitere Beispiele einfügen!