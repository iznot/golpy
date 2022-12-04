from time import sleep

import basic_game_functions as gm
import gameboard_manipulation as gam
import samples

import tkinter as tk 



class GolpyGui():

    
    def __init__(self, sample_key):

        self.window = tk.Tk()
        
        self.gameboard_label = tk.Label(text = '')

        self.set_gameboard(sample_key)    

        # Text Frame
        self.text_frame = tk.Frame(self.window)

        # Text field to paste
        self.text_field = tk.Text(self.text_frame, height = 4, width = 50)
        

        # Dropdown
        options = list(samples.sample_dict.keys())
        sample = tk.StringVar(self.window)
        sample.set(sample_key)
        self.sample_selector = tk.OptionMenu(self.text_frame, sample, command = self.selectSample, *options)

        self.text_field.grid(columnspan=3, row = 0, column = 1, padx='5', pady='5')
        self.sample_selector.grid(row = 0, column = 4, padx='5', pady='5')
        self.text_frame.pack()

        # Button Frame
        self.button_frame = tk.Frame(self.window)

        nxt_button = tk.Button(
            self.button_frame,
            text = "next",
            width=15,
            height = 3,
            bg="#668B8B",
            fg = "#F0F0F0",
            command = self.nextCallBack
        )

        self.run_button = tk.Button(
            self.button_frame,
            text = "run",
            width=15,
            height = 3,
            bg="#BC8F8F",
            fg = "#F0F0F0",
            command = self.runCallBack
        )

        self.running = False
    
        self.speed = tk.Scale(self.button_frame, from_= 1, to = 10, orient = tk.HORIZONTAL)

        nxt_button.grid(row=0, column = 0, padx='5', pady='5')
        self.run_button.grid(row = 0, column = 1, padx='5', pady='5')
        self.speed.grid(row = 0, column =2, padx='5', pady='5')
        self.button_frame.pack()


        tk.mainloop()
    
    
    def set_gameboard(self, sample_key):
        self.gameboard = samples.sample_dict[sample_key]
        self.gameboard_label.configure(
                            text = gm.get_gameboard_text_compact(self.gameboard),
                            font=("Webdings", 12))
        
        self.gameboard_label.pack()


    def nextCallBack(self):
        #TODO: add option to expand
        #self.gameboard = gam.expand_gameboard_if_necessary(self.gameboard)
        self.gameboard = gm.play(self.gameboard)
        
        self.gameboard_label["text"] = gm.get_gameboard_text_compact(self.gameboard)
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



