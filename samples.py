import basic_game_functions as gamefun

#Spaceship
def get_gleiter(size = 30):
    gameboard = gamefun.create_gameboard(rows = size, cols = size)
    gameboard[4,1] = True
    gameboard[4,2] = True
    gameboard[4,3] = True
    gameboard[3,3] = True
    gameboard[2,2] = True
    return gameboard

def get_segler(size = 30):
    gameboard = gamefun.create_gameboard(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2) 
    gameboard[x, y] = True
    gameboard[x, y - 1] = True
    gameboard[x, y - 2] = True
    gameboard[x, y - 3] = True
    gameboard[x + 1, y - 4] = True
    gameboard[x + 3, y - 4] = True
    gameboard[x + 1, y] = True
    gameboard[x + 2, y] = True
    gameboard[x + 3, y - 1] = True
    return gameboard




#random
def get_random(size = 30):
    gameboard = gamefun.create_gameboard(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2) 
    gameboard[x, y] = True
    gameboard[x - 1, y] = True
    gameboard[x - 2, y] = True
    gameboard[x - 3, y] = True
    gameboard[x - 4, y + 1] = True
    gameboard[x - 4, y + 3] = True
    gameboard[x, y + 1] = True
    gameboard[x, y + 2] = True
    gameboard[x - 1, y + 2] = True
    return gameboard

#destinct:
def get_erased(size = 40):
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

#Oszilatoren:
def get_pulsator(size = 40):
    gameboard = gamefun.create_gameboard(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2)
    gameboard[x - 1, y - 1] = True
    gameboard[x + 2, y - 1] = True
    gameboard[x - 1, y + 1] = True
    gameboard[x + 2, y + 1] = True
    gameboard[x - 2, y] = True
    gameboard[x - 3, y] = True
    gameboard[x - 4, y] = True
    gameboard[x - 5, y] = True
    gameboard[x - 6, y] = True
    gameboard[x - 5, y + 1] = True
    gameboard[x - 6, y + 1] = True
    gameboard[x - 5, y - 1] = True
    gameboard[x - 6, y - 1] = True
    gameboard[x + 3, y] = True
    gameboard[x + 4, y] = True
    gameboard[x + 5, y] = True
    gameboard[x + 6, y] = True
    gameboard[x + 7, y] = True
    gameboard[x + 6, y - 1] = True
    gameboard[x + 7, y - 1] = True
    gameboard[x + 6, y + 1] = True
    gameboard[x + 7, y + 1] = True
    return gameboard

def get_Tümmler(size = 40):
    gameboard = gamefun.create_gameboard(rows = size, cols = size)
    x = int(size / 2)
    y = int(size / 2)
    gameboard[x, y - 1] = True
    gameboard[x + 1, y - 1] = True
    gameboard[x + 2, y - 1] = True
    gameboard[x + 4, y - 1] = True
    gameboard[x + 4, y - 2] = True
    gameboard[x, y - 3] = True
    gameboard[x, y - 4] = True
    gameboard[x - 1, y - 2] = True
    gameboard[x - 1, y - 3] = True
    gameboard[x, y + 1] = True
    gameboard[x + 1, y + 1] = True
    gameboard[x + 2, y + 1] = True
    gameboard[x + 4, y + 1] = True
    gameboard[x + 4, y + 2] = True
    gameboard[x, y + 3] = True
    gameboard[x, y + 4] = True
    gameboard[x - 1, y + 2] = True
    gameboard[x - 1, y + 3] = True
    return gameboard

#Stable:
def get_Loaf(size = 10):
    gameboard = gamefun.create_gameboard(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2)
    gameboard[x, y] = True
    gameboard[x + 1, y + 1] = True
    gameboard[x - 1, y - 1] = True
    gameboard[x, y - 2] = True
    gameboard[x + 1, y - 2] = True
    gameboard[x + 2, y] = True
    gameboard[x + 2, y - 1] = True
    return gameboard


def get_Eater(size = 10):
    gameboard = gamefun.create_gameboard(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2)  
    gameboard[x, y] = True
    gameboard[x + 1, y] = True
    gameboard[x + 2, y] = True
    gameboard[x + 2, y + 1] = True
    gameboard[x - 1, y - 1] = True
    gameboard[x - 1, y - 2] = True
    gameboard[x, y - 2] = True

    return gameboard

# TODO: viele weitere Beispiele einfügen!


sample_dict = {
                'Gleiter' : get_gleiter(),
                'Segler' : get_segler(),
                'Erased' : get_erased(),
                'Pulsator' : get_pulsator(),
                'Tümmler' : get_Tümmler(),
                'Loaf' : get_Loaf(),
                'Eater' : get_Eater(),
                'Random' : get_random()}
