from time import sleep

import basic_game_functions as gamefun
import samples

import tkinter as tk 


class GolpyGui():

    
    def font_size_chooser(e):
        gameboard.config(
            size = font_size_gameboard.get(font_size_gameboard.curselection()))

    def __init__(self, sample_key):

        self.window = tk.Tk()
        self.gameboard_label = tk.Label(text = '')

        self.set_gameboard(sample_key)    

        # Dropdown
        options = list(samples.sample_dict.keys())
        sample = tk.StringVar(self.window)
        sample.set(sample_key)
        self.sample_selector = tk.OptionMenu(self.window, sample, command = self.selectSample, *options)
        

        self.sample_selector.pack()

        nxt_button = tk.Button(
            text = "next",
            width=15,
            height = 3,
            bg="#668B8B",
            fg = "#F0F0F0",
            command = self.nextCallBack
        )

        self.run_button = tk.Button(
            text = "run",
            width=15,
            height = 3,
            bg="#BC8F8F",
            fg = "#F0F0F0",
            command = self.runCallBack
        )

        self.running = False
    
        self.speed = tk.Scale(from_= 1, to = 10, orient = tk.HORIZONTAL)

        nxt_button.pack()
        self.run_button.pack()
        self.speed.pack()
    


        tk.mainloop()
    
    
    def set_gameboard(self, sample_key):
        self.gameboard = samples.sample_dict[sample_key]
        self.gameboard_label.configure(
                            text = gamefun.get_gameboard_text_compact(self.gameboard),
                            font=("Webdings", 12))
        
        self.gameboard_label.pack()


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


    def selectSample(self, val):
        #hide
        self.set_gameboard(val)

def main():
    #gleiter = samples.get_gleiter(16)
    #GolpyGui(gleiter)
    #erase = samples.get_erased()
    GolpyGui(list(samples.sample_dict.keys())[0])

if __name__ == "__main__":
    main()



