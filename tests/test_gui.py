import unittest
import numpy as np
import play as play
import tkinter as tk

class TestGUI(unittest.TestCase):

#get_neighbour_indices

    def test_gameboard(self):
        g0 = play.create_configuration(rows = 6, cols = 6)
        g0[0][3,4] = True
        g0[0][4,4] = True
        g0[0][5,4] = True
        window = tk.Tk()
        gameboard = tk.Label(text = play.get_gameboard_text(g0))
        gameboard.pack()
        print("done")