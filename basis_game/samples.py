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
    start_y = int(size / 2)
    gameboard[start_x - 2,start_y-1] = True
    gameboard[start_x - 2,start_y] = True
    gameboard[start_x - 2,start_y+1] = True
    gameboard[start_x - 1,start_y-1] = True
    gameboard[start_x - 1,start_y+1] = True
    gameboard[start_x,    start_y-1] = True
    gameboard[start_x,    start_y+1] = True
    gameboard[start_x + 2,start_y-1] = True
    gameboard[start_x + 2,start_y+1] = True
    gameboard[start_x + 3,start_y-1] = True
    gameboard[start_x + 3,start_y+1] = True
    gameboard[start_x + 4,start_y-1] = True
    gameboard[start_x + 4,start_y] = True
    gameboard[start_x + 4,start_y+1] = True
    return gameboard

# TODO: viele weitere Beispiele einfügen!