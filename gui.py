from time import sleep

import basic_game_functions as gm
import gameboard_manipulation as gam
import run_simulation as sim
import samples
import numpy as np
import tkinter as tk 


class DrawableGrid(tk.Frame):
    def __init__(self, parent, golpy, gameboard, size=5):
        super().__init__(parent, bd=1, relief="sunken")
        self.golpy = golpy
        self.gameboard = gameboard
        self.height = gameboard.shape[0]
        self.width = gameboard.shape[1]
        self.size = size
        canvas_width = self.width*size
        canvas_height = self.height*size
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, width=canvas_width, height=canvas_height)
        self.canvas.pack(fill="both", expand=True, padx=2, pady=2)

        for row in range(self.height):
            for column in range(self.width):
                x0, y0 = (column * self.size), (row*self.size)
                x1, y1 = (x0 + self.size), (y0 + self.size)
                color = "black" if gameboard[row, column] == True else "white"
                self.canvas.create_rectangle(x0, y0, x1, y1,
                                             fill=color, outline="gray",
                                             tags=(self._tag(row, column),"cell" ))

        self.canvas.tag_bind("cell", "<B1-Motion>", self.paint)
        self.canvas.tag_bind("cell", "<1>", self.paint)

    def _tag(self, row, column):
        """Return the tag for a given row and column"""
        tag = f"{row},{column}"
        return tag

    def get_pixels(self):
        row = ""
        for row in range(self.height):
            output = ""
            for column in range(self.width):
                color = self.canvas.itemcget(self._tag(row, column), "fill")
                value = "1" if color == "black" else "0"
                output += value
        return output
    
    def set_gameboard(self, gameboard):
        
        idx = np.where(self.gameboard != gameboard)

        for i in range(0, len(idx[0])):
            row = idx[0][i]
            column = idx[1][i]
            x0, y0 = (column * self.size), (row*self.size)
            #x1, y1 = (x0 + self.size), (y0 + self.size)
            color = "black" if gameboard[row, column] == True else "white"
            cell = self.canvas.find_closest(x0, y0)
            self.canvas.itemconfigure(cell, fill = color)

        self.gameboard = gameboard


    def get_gameboard(self):
        gb = np.full((self.height, self.width), False)
        for row in range(self.height):
            for column in range(self.width):
                color = self.canvas.itemcget(self._tag(row, column), "fill")
                if color == "black":
                    gb[row, column] = True
        return gb
        

    def paint(self, event):
        cell = self.canvas.find_closest(event.x, event.y)
        color = self.canvas.itemcget(cell, "fill")
        color = "black" if color == "white" else "white"
        self.canvas.itemconfigure(cell, fill=color)
        self.golpy.set_text_to_value("")
        self.gameboard = self.golpy.gameboard = self.get_gameboard()
        




class GolpyGui():

    
    def __init__(self, sample_key):

        self.window = tk.Tk()
        self.window.title("golpy - Game of Life Python - Anaïs Glur")
        
        

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

        self.paint_button = tk.Button(
            self.text_frame,
            text = "paint",
            width=15,
            height = 3,
            bg="#668B8B",
            fg = "#F0F0F0",
            command = self.paint_gameboard
        )

        self.get_text_button = tk.Button(
            self.text_frame,
            text = "get text",
            width=15,
            height = 3,
            bg="#668B8B",
            fg = "#F0F0F0",
            command = self.set_text
        )

        self.get_print_button = tk.Button(
            self.text_frame,
            text = "get print",
            width=15,
            height = 3,
            bg="#668B8B",
            fg = "#F0F0F0",
            command = self.set_print
        )

        self.text_field.grid(columnspan=3, row = 0, column = 0, padx='5', pady='5')
        self.scroll_bar.grid(row = 0, column = 3, rowspan = 2, sticky = tk.N + tk.S+tk.W)
        self.paint_button.grid(row = 0, column = 4, rowspan = 1)
        self.get_text_button.grid(row = 0, column = 5, rowspan = 1)
        self.get_print_button.grid(row = 0, column = 6, rowspan = 1)
        self.sample_selector.grid(row = 0, column = 7 , padx='5', pady='5')
        
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
     

        self.gameboard = gm.create_gameboard(20, 20)
        self.canvas = DrawableGrid(self.window, self, self.gameboard, size=20)
        self.canvas.pack(fill="both", expand=True)


        tk.mainloop()
    
    
    def paint_gameboard(self):
        gb_txt = self.text_field.get(1.0, tk.END)
        
        self.gameboard = sim.convert_to_gameboard(gb_txt)
        
        self.canvas.pack_forget()
        self.canvas = DrawableGrid(self.window, self, self.gameboard, size = 20)
        self.canvas.pack(fill="both", expand=True)


    def set_text_to_value(self, text_str):
        self.text_field.delete(1.0, tk.END)
        self.text_field.insert(tk.END, text_str)

    def set_text(self):
        self.gameboard = self.canvas.get_gameboard()
        gb_str = sim.convert_to_string(self.gameboard)
        self.set_text_to_value(gb_str)
   
    def set_print(self):
        self.gameboard = self.canvas.get_gameboard()
        gb_str = gm.get_gameboard_text(self.gameboard)
        self.set_text_to_value(gb_str)

    def nextCallBack(self):
        self.set_text_to_value("")
        gb_orig = self.gameboard
        if self.expand.get() == 1:
            self.gameboard = gam.expand_gameboard_if_necessary(self.gameboard)
        gb = gm.play(self.gameboard)
        if gm.gameboard_equal(gb, self.gameboard):
            self.running = False
            self.run_button["text"] = "run"
        
        self.gameboard = gb
        
        if self.gameboard.shape != gb_orig.shape:
            
            self.canvas.pack_forget()
            self.canvas = DrawableGrid(self.window, self, self.gameboard, size = 20)
            self.canvas.pack(fill="both", expand=True)

        else:
            self.canvas.set_gameboard(self.gameboard)

        
        
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
            if self.speed.get() == 10:
                self.window.after(10, self.play)
            else:
                self.window.after((int)(10 / self.speed.get() * 100), self.play)


    def selectSample(self, val):
        #hide
        #self.set_gameboard(val)
        gb = samples.sample_dict[val]
        gb_str = sim.convert_to_string(gb)        
        self.set_text_to_value(gb_str)

def main():
    #gleiter = samples.get_gleiter(16)
    #GolpyGui(gleiter)
    #erase = samples.get_erased()
    GolpyGui(list(samples.sample_dict.keys())[0])

if __name__ == "__main__":
    main()



