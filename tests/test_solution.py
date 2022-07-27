import unittest
import basis_game.basic_game_functions as gamefun

class TestSolution(unittest.TestCase):


    def test_get_neighbour_indices(self):
        res = gamefun.get_neighbour_indices(4, 5, 9, 9)
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