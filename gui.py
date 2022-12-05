from time import sleep

import basic_game_functions as gm
import gameboard_manipulation as gam
import run_simulation as sim
import samples

import tkinter as tk 



class GolpyGui():

    
    def __init__(self, sample_key):

        self.window = tk.Tk()
        self.window.title("golpy - Game of Life Python - Anaïs Glur")
        
        self.gameboard_label = tk.Label(text = '')

        #self.set_gameboard(sample_key)    

        # Text Frame
        self.text_frame = tk.Frame(self.window)

        # Text field to paste
        self.text_field = tk.Text(self.text_frame, height = 4, width = 50,  )
        self.scroll_bar = tk.Scrollbar(self.text_frame)
        self.text_field.config(yscrollcommand= self.scroll_bar.set)
        self.scroll_bar.config(command= self.text_field.yview)

        # Dropdown
        options = list(samples.sample_dict.keys())
        sample = tk.StringVar(self.window)
        sample.set(sample_key)
        self.sample_selector = tk.OptionMenu(self.text_frame, sample, command = self.selectSample, *options)

        self.accept_button = tk.Button(
            self.text_frame,
            text = "accept",
            width=15,
            height = 3,
            bg="#668B8B",
            fg = "#F0F0F0",
            command = self.set_gameboard
        )

        self.text_field.grid(columnspan=3, row = 0, column = 0, padx='5', pady='5')
        self.scroll_bar.grid(row = 0, column = 3, rowspan = 2, sticky = tk.N + tk.S+tk.W)
        self.accept_button.grid(row = 0, column = 4, rowspan = 2)
        self.sample_selector.grid(row = 0, column = 6 , padx='5', pady='5')
        
        self.text_frame.pack()

        # Button Frame
        self.button_frame = tk.Frame(self.window)

        self.nxt_button = tk.Button(
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

        self.expand = tk.IntVar()
        self.expand_checkbox = tk.Checkbutton(self.button_frame, text = "expand", variable= self.expand)

        self.nxt_button.grid(row=0, column = 0, padx='5', pady='5')
        self.run_button.grid(row = 0, column = 1, padx='5', pady='5')
        self.speed.grid(row = 0, column =2, padx='5', pady='5')
        self.expand_checkbox.grid(row = 0, column = 3, padx='5', pady='5')
        self.button_frame.pack()


        tk.mainloop()
    
    
    def set_gameboard(self):
        gb_txt = self.text_field.get(1.0, tk.END)
        self.gameboard = sim.convert_to_gameboard(gb_txt)
        
        font_size = self.get_font_size(self.gameboard)
        self.gameboard_label.configure(
                            text = gm.get_gameboard_text_compact(self.gameboard),
                            font=("Webdings", font_size))
        
        self.gameboard_label.pack()

    def get_font_size(self, gameboard):
        max_dim = max(gameboard.shape)
        if max_dim < 50:
            return 12
        font_size = 14 - max_dim // 20
        return font_size

    def nextCallBack(self):
        
        self.gameboard = gm.play(self.gameboard)
        if self.expand.get() == 1:
            self.gameboard = gam.expand_gameboard_if_necessary(self.gameboard)
        gb_str = sim.convert_to_string(self.gameboard)        
        self.text_field.delete(1.0, tk.END)
        self.text_field.insert(tk.END, gb_str)

        self.gameboard_label["font"] = ("Webdings", self.get_font_size(self.gameboard))
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
        #self.set_gameboard(val)
        gb = samples.sample_dict[val]
        gb_str = sim.convert_to_string(gb)        
        self.text_field.delete(1.0, tk.END)
        self.text_field.insert(tk.END, gb_str)

def main():
    #gleiter = samples.get_gleiter(16)
    #GolpyGui(gleiter)
    #erase = samples.get_erased()
    GolpyGui(list(samples.sample_dict.keys())[0])

if __name__ == "__main__":
    main()



