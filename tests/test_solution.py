from turtle import Turtle
import unittest
import numpy as np
import basis_game.basic_game_functions as gamefun

class TestSolution(unittest.TestCase):

#get_neighbour_indices

    def test_get_neighbour_indices(self):
        res = gamefun.get_neighbour_indices(row = 4, col = 5, rows = 9, cols = 9)
        assert len(res) == 4
        #toprow
        assert res[0] == 3
        #bottomrow
        assert res[1] == 5
        #leftcol
        assert res[2] == 4
        #rightcol
        assert res[3] == 6


    def test_get_neighbour_indices_corner_cases_top_left(self):
        res = gamefun.get_neighbour_indices(0, 0, 9, 6)
        assert len(res) == 4
        #toprow
        assert res[0] == 8
        #bottomrow
        assert res[1] == 1
        #leftcol
        assert res[2] == 5
        #rightcol
        assert res[3] == 1

    def test_get_neighbour_indices_corner_cases_bottom_right(self):
        res = gamefun.get_neighbour_indices(8, 5, 9, 6)
        assert len(res) == 4
        #toprow
        assert res[0] == 7
        #bottomrow
        assert res[1] == 0
        #leftcol
        assert res[2] == 4
        #rightcol
        assert res[3] == 0


#print_gameboard

    def test_create_gameboard(self):
        
        gameboard = gamefun.create_gameboard(rows = 9, cols = 10)
        
        assert gameboard.size == 90
        assert gameboard.shape == (9, 10)


    def test_demo_print_gameboard(self):
        gameboard = gamefun.create_gameboard(rows = 9, cols = 10)
        gameboard[3,4] = True
        gameboard[5,4] = True
        gameboard[4,4] = True
        
        print(gameboard)

    
    def test_demo_gameplay(self):
        g0 = gamefun.create_gameboard(rows = 9, cols = 10)
        g0[3,4] = True
        g0[4,4] = True
        g0[5,4] = True

        assert g0.sum() == 3

        g1 = gamefun.play(g0)

        assert g1.sum() == 3
        assert g1[4,3] == True
        assert g1[4,4] == True
        assert g1[4,5] == True

        g2 = gamefun.play(g1)
        
        assert g2.sum() == 3
    

    def test_why_space(self):
        g0 = gamefun.create_gameboard(rows = 7, cols = 5)
        g0[1,2] = True
        g0[3,1] = True

        assert g0.sum() == 2
    # immer bei Hälfte(runtergerundet) einen Space

    def test_gameplay_corner(self):
        g0 = gamefun.create_gameboard(rows = 8, cols = 7)
        g0[7,6] = True
        g0[7,5] = True
        g0[7,0] = True
        g0[0,0] = True
        g0[0,1] = True

        assert g0.sum() == 5  

        g1 = gamefun.play(g0)

        assert g1.sum() == 6
        assert g1[7,0] == True
        assert g1[0,0] == True
        assert g1[0,1] == True
        assert g1[7,0] == True
        assert g1[6,6] == True
        assert g1[7,6] == True


    def test_equal(self):
        g0 = gamefun.create_gameboard(rows = 8, cols = 7)
        g0[7,6] = True
        g0[7,5] = True
        g0[7,0] = True

        is_equal = gamefun.gameboard_equal(g0, g0)
        assert is_equal == True
    
    def test_not_equal(self):
        g0 = gamefun.create_gameboard(rows = 8, cols = 7)
        g0[7,6] = True
        g0[7,5] = True
        g0[7,0] = True

        g1 = gamefun.play(g0)
        
        is_equal = gamefun.gameboard_equal(g0, g1)
        assert is_equal == False