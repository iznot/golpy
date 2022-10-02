from time import sleep
import numpy as np
import basic_game_functions as gamefun
import os 
import tkinter as tk 


gameboard = gamefun.create_gameboard(rows = 9, cols = 10)

def gui():
    window = tk.Tk()
    gameboard_label = tk.Label(text = gamefun.get_gameboard_text(gameboard, separator = False))
    gameboard_label.configure(font=("Consolas", 12))
    gameboard_label.pack()
    

    button = tk.Button(
        text = "next",
        width=15,
        height = 3,
        bg="blue",
        fg = "yellow",
        command = lambda: nextCallBack(gameboard_label)
    )
    
    button.pack()
    
    tk.mainloop()
    
    
def nextCallBack(gameboard_label):
    gameboard2 = gamefun.play(gameboard)
    gameboard_label["text"] = gamefun.get_gameboard_text(gameboard2, separator=False)
    gameboard_label.pack()
    gameboard = gameboard2


def main():
    
    gameboard[3,4] = True
    gameboard[4,4] = True
    gameboard[5,4] = True
    gui()

if __name__ == "__main__":
    main()



