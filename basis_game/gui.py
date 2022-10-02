import numpy as np
import basic_game_functions as gamefun
import os 
import tkinter as tk 


def gui(gameboard : np.array):
    window = tk.Tk()
    gameboard_gui = tk.Label(text = gamefun.get_gameboard_text(gameboard, separator = False))
    gameboard_gui.configure(font=("Consolas", 12))
    gameboard_gui.pack()
    window.mainloop()
    print("End")



def main():
    g0 = gamefun.create_gameboard(rows = 9, cols = 10)
    g0[3,4] = True
    g0[4,4] = True
    g0[5,4] = True
    gui(g0)

if __name__ == "__main__":
    main()



