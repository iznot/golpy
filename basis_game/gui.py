from time import sleep

import basic_game_functions as gamefun
import samples

import tkinter as tk 


class GolpyGui():

    


    def __init__(self, gameboard):

        self.window = tk.Tk()
        self.gameboard = gameboard
        self.gameboard_label = tk.Label(text = gamefun.get_gameboard_text_compact(self.gameboard))
        self.gameboard_label.configure(font=("Webdings", 12))
        
        self.gameboard_label.pack()
    

        nxt_button = tk.Button(
            text = "next",
            width=15,
            height = 3,
            bg="blue",
            fg = "yellow",
            command = self.nextCallBack
        )

        self.run_button = tk.Button(
            text = "run",
            width=15,
            height = 3,
            bg="blue",
            fg = "yellow",
            command = self.runCallBack
        )

        self.running = False
    
        self.speed = tk.Scale(from_= 1, to = 10, orient = tk.HORIZONTAL)

        nxt_button.pack()
        self.run_button.pack()
        self.speed.pack()
    


        tk.mainloop()
    
    
    def nextCallBack(self):
        
        self.gameboard = gamefun.play(self.gameboard)
        self.gameboard_label["text"] = gamefun.get_gameboard_text_compact(self.gameboard)
        self.gameboard_label.pack()
        
    def runCallBack(self):
        if self.running:
            self.running = False
            self.run_button["text"] = "run"
        else:
            self.running = True
            self.run_button["text"] = "stop"
            self.window.after(0, self.play)

    def play(self):
        if self.running:
            self.nextCallBack()
            self.window.after((int)(10 / self.speed.get() * 100), self.play)


def main():
    #gleiter = samples.get_gleiter(16)
    #GolpyGui(gleiter)
    erase = samples.get_erased(20)
    GolpyGui(erase)

if __name__ == "__main__":
    main()



