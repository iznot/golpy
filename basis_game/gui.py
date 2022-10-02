from time import sleep

import basic_game_functions as gamefun
import samples

import tkinter as tk 


class GolpyGui():

    def __init__(self, gameboard):

        window = tk.Tk()
        self.gameboard = gameboard
        self.gameboard_label = tk.Label(text = gamefun.get_gameboard_text_compact(self.gameboard))
        self.gameboard_label.configure(font=("Webdings", 12))
        
        self.gameboard_label.pack()
    

        button = tk.Button(
            text = "next",
            width=15,
            height = 3,
            bg="blue",
            fg = "yellow",
            command = self.nextCallBack
        )
    
        button.pack()
    
        tk.mainloop()
    
    
    def nextCallBack(self):
        
        self.gameboard = gamefun.play(self.gameboard)
        self.gameboard_label["text"] = gamefun.get_gameboard_text_compact(self.gameboard)
        self.gameboard_label.pack()
        


def main():
    gleiter = samples.get_gleiter(16)
    GolpyGui(gleiter)

if __name__ == "__main__":
    main()



