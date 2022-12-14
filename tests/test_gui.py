import unittest
import numpy as np
import basic_game_functions as gm
import tkinter as tk

class TestGUI(unittest.TestCase):

#get_neighbour_indices

    def test_gameboard(self):
        g0 = gm.create_gameboard(rows = 6, cols = 6)
        g0[0][3,4] = True
        g0[0][4,4] = True
        g0[0][5,4] = True
        window = tk.Tk()
        gameboard = tk.Label(text = gm.get_gameboard_text(g0))
        gameboard.pack()
        print("done")