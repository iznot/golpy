# gui.py

"""
Das GUI (graphical user interface) von Golpy.mkdocsmk
"""

import tkinter as tk

import numpy as np

import gameboard_manipulation as gam
import play as play
import samples
import simulation as sim


class DrawableGrid(tk.Frame):
    def __init__(self, parent, golpy, gameboard, size=5):
        super().__init__(parent, bd=1, relief="sunken")
        self.golpy = golpy
        self.gameboard = gameboard
        self.height = gameboard[0].shape[0]
        self.width = gameboard[0].shape[1]
        self.size = size
        canvas_width = self.width*size
        canvas_height = self.height*size
        self.canvas = tk.Canvas(self, bd=0, highlightthickness=0, width=canvas_width, height=canvas_height)
        self.canvas.pack(fill="both", expand=True, padx=2, pady=2)

        for row in range(self.height):
            for column in range(self.width):
                x0, y0 = (column * self.size), (row*self.size)
                x1, y1 = (x0 + self.size), (y0 + self.size)
                color = "black" if gameboard[0][row, column] == True else "white"
                
                self.canvas.create_rectangle(x0, y0, x1, y1,
                                             fill=color, outline="gray", 
                                             tags=(self._tag(row, column),"cell" ))
                

        self.canvas.tag_bind("cell", "<B1-Motion>", self.paint)
        self.canvas.tag_bind("cell", "<1>", self.paint)

    def show_neighbour_count(self):
        next_gen = play.play(self.gameboard)
        nc = play.get_neighbour_count(self.gameboard)

        idxs = np.where(nc > 0)

        for idx in zip(idxs[0], idxs[1]):
            #color = "green" if next_gen[0][idx] == True else "red"
            if self.gameboard[0][idx] == True:
                color = "#00FF00" if next_gen[0][idx] == True else "#FFB6C1"
            else:
                color = "#008000" if next_gen[0][idx] == True else "#FF0000"
            row = idx[0]
            column = idx[1]
            x0, y0 = (column * self.size), (row*self.size)
            self.canvas.create_text(x0 + 0.5*self.size, y0 + 0.5*self.size, fill=color,font="Consolas 14",
            text=str(nc[row, column]), tags = (self._tag(row, column),"cell" ))


    def hide_neighbour_count(self):
        for row in range(self.height):
            for column in range(self.width):
                x0, y0 = (column * self.size) + 0.5*self.size, (row*self.size) + 0.5*self.size
                #x1, y1 = (x0 + self.size), (y0 + self.size)
                cell = self.canvas.find_closest(x0, y0)
                if self.canvas.type(cell) == 'text':
                    self.canvas.delete(cell)
                


    def _tag(self, row, column):
        """Return the tag for a given row and column"""
        tag = f"{row},{column}"
        return tag

    def get_pixels(self):
        #row = ""
        for row in range(self.height):
            output = ""
            for column in range(self.width):
                color = self.canvas.itemcget(self._tag(row, column), "fill")
                value = "1" if color == "black" else "0"
                output += value
        return output
    
    def set_gameboard(self, gameboard):
        
        idx = np.where(self.gameboard[0] != gameboard[0])

        for i in range(0, len(idx[0])):
            row = idx[0][i]
            column = idx[1][i]
            x0, y0 = (column * self.size), (row*self.size)
            #x1, y1 = (x0 + self.size), (y0 + self.size)
            color = "black" if gameboard[0][row, column] == True else "white"
            cell = self.canvas.find_closest(x0, y0)
            self.canvas.itemconfigure(cell, fill = color)

        self.gameboard = gameboard


    def get_gameboard(self):
        gb_a = np.full((self.height, self.width), False)
        for row in range(self.height):
            for column in range(self.width):
                color = self.canvas.itemcget(self._tag(row, column), "fill")
                if color == "black":
                    gb_a[row, column] = True
        gameboard = play.create_configuration(gb_a)
        return gameboard
        

    def paint(self, event):
        self.golpy.neighbour_count(False)
        cell = self.canvas.find_closest(event.x, event.y)
        if self.canvas.type(cell) == 'text':
            cell = self.canvas.find_below(cell)

        color = self.canvas.itemcget(cell, "fill")
        color = "black" if color == "white" else "white"
        self.canvas.itemconfigure(cell, fill=color)
        self.golpy.set_text_to_value("")
        self.gameboard = self.golpy.gameboard = self.get_gameboard()
        self.golpy.reset_counter()
        




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

        self.number_button = tk.Button(
            self.button_frame,
            text = "show #",
            width=15,
            height = 3,
            bg="#BC8F8F",
            fg = "#F0F0F0",
            command = self.toggle_neighbour_count
        )

        self.show_numbers = False

        self.running = False
    
        self.speed_label = tk.Label(self.button_frame, text = "Speed:")
        self.speed = tk.Scale(self.button_frame, from_= 1, to = 10, orient = tk.HORIZONTAL)
        
        self.size_label = tk.Label(self.button_frame, text = "Size:")
        self.size = tk.Scale(self.button_frame, from_= 5, to = 25, orient = tk.HORIZONTAL, command= self.set_size )
        self.size.set(20)
        
        self.counter_lbl = tk.Label(self.button_frame, text = "0", font=('Consolas 24'))
        self.counter = 0
        

        self.expand = tk.IntVar()
        self.expand_checkbox = tk.Checkbutton(self.button_frame, text = "expand", variable= self.expand)

        self.nxt_button.grid(row=0, column = 0, padx='5', pady='5', rowspan=2)
        self.run_button.grid(row = 0, column = 1, padx='5', pady='5', rowspan=2)
        self.number_button.grid(row = 0, column = 2, padx= '5', pady='5', rowspan=2)
        
        self.speed_label.grid(row = 0, column = 3)
        self.speed.grid(row = 1, column =3, padx='5', pady='5')
        
        self.size_label.grid(row = 0, column = 4)
        self.size.grid(row = 1, column =4, padx='5', pady='5')
        self.expand_checkbox.grid(row = 0, column = 5, padx='5', pady='5')

        self.counter_lbl.grid(row = 0, column=6, rowspan=2)
        self.button_frame.pack()
     

        self.gameboard = play.create_configuration(rows= 20, cols = 20)
        self.canvas = DrawableGrid(self.window, self, self.gameboard, size = self.size.get())
        self.canvas.pack(fill="both", expand=True)


        tk.mainloop()
    
    def reset_counter(self):
        self.counter = 0
        self.counter_lbl['text'] = self.counter

    def increase_counter(self):
        self.counter += 1
        self.counter_lbl['text'] = self.counter

    def set_size(self, size):
        self.canvas.pack_forget()
        self.canvas = DrawableGrid(self.window, self, self.gameboard, size = self.size.get())
        self.canvas.pack(fill="both", expand=False)
        self.neighbour_count(False)

    def toggle_neighbour_count(self):
        self.neighbour_count(not self.show_numbers)

    def neighbour_count(self, target_state):
        if self.show_numbers == False and target_state == True:
            self.canvas.show_neighbour_count()
            self.number_button['text'] = "hide #"
            self.show_numbers = True
        elif self.show_numbers == True and target_state == False:
            self.canvas.hide_neighbour_count()
            self.number_button['text'] = "show #"
            self.show_numbers = False
        else:
            return target_state

    def paint_gameboard(self):
        gb_txt = self.text_field.get(1.0, tk.END)
        
        self.gameboard = gam.create_configuration_from_string(gb_txt)
        
        self.canvas.pack_forget()
        self.canvas = DrawableGrid(self.window, self, self.gameboard, size = self.size.get())
        self.reset_counter()
        self.canvas.pack(fill="both", expand=True)


    def set_text_to_value(self, text_str):
        self.text_field.delete(1.0, tk.END)
        self.text_field.insert(tk.END, text_str)

    def set_text(self):
        self.gameboard = self.canvas.get_gameboard()
        gb_str = gam.convert_to_string_representation(self.gameboard)
        self.set_text_to_value(gb_str)
   
    def set_print(self):
        self.gameboard = self.canvas.get_gameboard()
        gb_str = play.get_gameboard_text(self.gameboard)
        self.set_text_to_value(gb_str)

    def nextCallBack(self):
        self.set_text_to_value("")
        self.neighbour_count(False)
        gb_orig = self.gameboard
        if self.expand.get() == 1:
            self.gameboard = gam.expand_gameboard_if_necessary(self.gameboard)
        gb = play.play(self.gameboard)
        self.increase_counter()

        if gam.configuration_equal(gb, self.gameboard):
            self.running = False
            self.run_button["text"] = "run"
        
        self.gameboard = gb
        
        if self.gameboard[0].shape != gb_orig[0].shape:
            
            self.canvas.pack_forget()
            self.canvas = DrawableGrid(self.window, self, self.gameboard, size = self.size.get())
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
        gb_str = gam.convert_to_string_representation(gb)        
        self.set_text_to_value(gb_str)

def main():
    """Started das GUI (Graphical User Interface) von golpy.
    Dieses kann verwendet werden, um Spielverläufe zu visualisieren. Oder um Konfigurationen durch Klicken zu definieren.
    """    
    #gleiter = samples.get_gleiter(16)
    #GolpyGui(gleiter)
    #erase = samples.get_erased()
    GolpyGui(list(samples.sample_dict.keys())[0])

if __name__ == "__main__":
    main()



