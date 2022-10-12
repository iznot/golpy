import unittest
import numpy as np
import basic_game_functions as gamefun
import tkinter as tk

class TestGUI(unittest.TestCase):

#get_neighbour_indices

    def test_gameboard(self):
        g0 = gamefun.create_gameboard(rows = 6, cols = 6)
        g0[3,4] = True
        g0[4,4] = True
        g0[5,4] = True
        window = tk.Tk()
        gameboard = tk.Label(text = gamefun.get_gameboard_text(g0))
        gameboard.pack()
        print("done")