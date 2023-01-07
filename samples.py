import play

#Spaceship
def get_gleiter(size = 30):
    gameboard = play.create_configuration(rows = size, cols = size)
    gameboard[0][2,0] = True
    gameboard[0][2,1] = True
    gameboard[0][2,2] = True
    gameboard[0][1,2] = True
    gameboard[0][0,1] = True
    return gameboard

def get_segler(size = 30):
    gameboard = play.create_configuration(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2) 
    gameboard[0][x, y] = True
    gameboard[0][x, y - 1] = True
    gameboard[0][x, y - 2] = True
    gameboard[0][x, y - 3] = True
    gameboard[0][x + 1, y - 4] = True
    gameboard[0][x + 3, y - 4] = True
    gameboard[0][x + 1, y] = True
    gameboard[0][x + 2, y] = True
    gameboard[0][x + 3, y - 1] = True
    return gameboard


#random
def get_random(size = 30):
    gameboard = play.create_configuration(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2) 
    gameboard[0][x, y] = True
    gameboard[0][x - 1, y] = True
    gameboard[0][x - 2, y] = True
    gameboard[0][x - 3, y] = True
    gameboard[0][x - 4, y + 1] = True
    gameboard[0][x - 4, y + 3] = True
    gameboard[0][x, y + 1] = True
    gameboard[0][x, y + 2] = True
    gameboard[0][x - 1, y + 2] = True
    return gameboard

#destinct:
def get_erased(size = 40):
    gameboard = play.create_configuration(rows = size, cols = size)
    start_x = int(size / 2)
    start_y = int(size / 2)
    gameboard[0][start_x - 2,start_y-1] = True
    gameboard[0][start_x - 2,start_y] = True
    gameboard[0][start_x - 2,start_y+1] = True
    gameboard[0][start_x - 1,start_y-1] = True
    gameboard[0][start_x - 1,start_y+1] = True
    gameboard[0][start_x,    start_y-1] = True
    gameboard[0][start_x,    start_y+1] = True
    gameboard[0][start_x + 2,start_y-1] = True
    gameboard[0][start_x + 2,start_y+1] = True
    gameboard[0][start_x + 3,start_y-1] = True
    gameboard[0][start_x + 3,start_y+1] = True
    gameboard[0][start_x + 4,start_y-1] = True
    gameboard[0][start_x + 4,start_y] = True
    gameboard[0][start_x + 4,start_y+1] = True
    return gameboard

#Oszilatoren:
def get_pulsator(size = 40):
    gameboard = play.create_configuration(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2)
    gameboard[0][x - 1, y - 1] = True
    gameboard[0][x + 2, y - 1] = True
    gameboard[0][x - 1, y + 1] = True
    gameboard[0][x + 2, y + 1] = True
    gameboard[0][x - 2, y] = True
    gameboard[0][x - 3, y] = True
    gameboard[0][x - 4, y] = True
    gameboard[0][x - 5, y] = True
    gameboard[0][x - 6, y] = True
    gameboard[0][x - 5, y + 1] = True
    gameboard[0][x - 6, y + 1] = True
    gameboard[0][x - 5, y - 1] = True
    gameboard[0][x - 6, y - 1] = True
    gameboard[0][x + 3, y] = True
    gameboard[0][x + 4, y] = True
    gameboard[0][x + 5, y] = True
    gameboard[0][x + 6, y] = True
    gameboard[0][x + 7, y] = True
    gameboard[0][x + 6, y - 1] = True
    gameboard[0][x + 7, y - 1] = True
    gameboard[0][x + 6, y + 1] = True
    gameboard[0][x + 7, y + 1] = True
    return gameboard

def get_Tuemmler(size = 40):
    gameboard = play.create_configuration(rows = size, cols = size)
    x = int(size / 2)
    y = int(size / 2)
    gameboard[0][x, y - 1] = True
    gameboard[0][x + 1, y - 1] = True
    gameboard[0][x + 2, y - 1] = True
    gameboard[0][x + 4, y - 1] = True
    gameboard[0][x + 4, y - 2] = True
    gameboard[0][x, y - 3] = True
    gameboard[0][x, y - 4] = True
    gameboard[0][x - 1, y - 2] = True
    gameboard[0][x - 1, y - 3] = True
    gameboard[0][x, y + 1] = True
    gameboard[0][x + 1, y + 1] = True
    gameboard[0][x + 2, y + 1] = True
    gameboard[0][x + 4, y + 1] = True
    gameboard[0][x + 4, y + 2] = True
    gameboard[0][x, y + 3] = True
    gameboard[0][x, y + 4] = True
    gameboard[0][x - 1, y + 2] = True
    gameboard[0][x - 1, y + 3] = True
    return gameboard

#Stable:
def get_Loaf(size = 10):
    gameboard = play.create_configuration(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2)
    gameboard[0][x, y] = True
    gameboard[0][x + 1, y + 1] = True
    gameboard[0][x - 1, y - 1] = True
    gameboard[0][x, y - 2] = True
    gameboard[0][x + 1, y - 2] = True
    gameboard[0][x + 2, y] = True
    gameboard[0][x + 2, y - 1] = True
    return gameboard


def get_Eater(size = 10):
    gameboard = play.create_configuration(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2)  
    gameboard[0][x, y] = True
    gameboard[0][x + 1, y] = True
    gameboard[0][x + 2, y] = True
    gameboard[0][x + 2, y + 1] = True
    gameboard[0][x - 1, y - 1] = True
    gameboard[0][x - 1, y - 2] = True
    gameboard[0][x, y - 2] = True

    return gameboard

#explodierend
def get_f_Pentomino(size = 50):
    gameboard = play.create_configuration(rows = size, cols = size)
    x = int(size/2)
    y = int(size/2) 
    gameboard[0][x, y + 1] = True
    gameboard[0][x, y] = True
    gameboard[0][x - 1, y] = True
    gameboard[0][x - 2, y] = True
    gameboard[0][x - 1, y - 1] = True
    
    return gameboard


sample_dict = {
                'Gleiter' : get_gleiter(),
                'Segler' : get_segler(),
                'Erased' : get_erased(),
                'Pulsator' : get_pulsator(),
                'Tümmler' : get_Tuemmler(),
                'Loaf' : get_Loaf(),
                'Eater' : get_Eater(),
                'f-Pentomino' : get_f_Pentomino(),
                'Random' : get_random()}
