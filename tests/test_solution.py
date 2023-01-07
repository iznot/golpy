import unittest

import gameboard_manipulation as gam
import play


class TestSolution(unittest.TestCase):


#print_configuration

    def test_create_configuration(self):
        
        configuration = play.create_configuration(rows = 9, cols = 10)
        
        assert configuration[0].size == 90
        assert configuration[0].shape == (9, 10)


    def test_demo_print_configuration(self):
        configuration = play.create_configuration(rows = 9, cols = 10)
        configuration[0][3,4] = True
        configuration[0][5,4] = True
        configuration[0][4,4] = True
        
        print(configuration)

    
    def test_demo_gameplay(self):
        g0 = play.create_configuration(rows = 9, cols = 10)
        g0[0][3,4] = True
        g0[0][4,4] = True
        g0[0][5,4] = True

        assert g0[0].sum() == 3

        g1 = play.play(g0)

        assert g1[0].sum() == 3
        assert g1[0][4,3] == True
        assert g1[0][4,4] == True
        assert g1[0][4,5] == True

        g2 = play.play(g1)
        
        assert g2[0].sum() == 3
    

    def test_why_space(self):
        g0 = play.create_configuration(rows = 7, cols = 5)
        g0[0][1,2] = True
        g0[0][3,1] = True

        assert g0[0].sum() == 2
    # immer bei Hälfte(runtergerundet) einen Space

    def test_gameplay_corner(self):
        g0 = play.create_configuration(rows = 8, cols = 7)
        g0[0][7,6] = True
        g0[0][7,5] = True
        g0[0][7,0] = True
        g0[0][0,0] = True
        g0[0][0,1] = True

        assert g0[0].sum() == 5  

        g1 = play.play(g0)

        assert g1[0].sum() == 6
        assert g1[0][7,0] == True
        assert g1[0][0,0] == True
        assert g1[0][0,1] == True
        assert g1[0][7,0] == True
        assert g1[0][6,6] == True
        assert g1[0][7,6] == True


    def test_equal(self):
        g0 = play.create_configuration(rows = 8, cols = 7)
        g0[0][7,6] = True
        g0[0][7,5] = True
        g0[0][7,0] = True

        is_equal = gam.configuration_equal(g0, g0, True)
        assert is_equal == True

        is_equal = gam.configuration_equal(g0, g0, False)
        assert is_equal == True


    def test_not_equal(self):
        g0 = play.create_configuration(rows = 8, cols = 7)
        g0[0][7,6] = True
        g0[0][7,5] = True
        g0[0][7,0] = True

        g1 = play.play(g0)
        
        is_equal = gam.configuration_equal(g0, g1, True)
        assert is_equal == False



    def test_expand(self):
        g0 = play.create_configuration(rows = 3, cols = 3)
        g0[0][0,0] = True
        g0[0][0,2] = True
        g0[0][2,2] = True
        play.print_gameboard(g0)
        gb = gam.expand_gameboard_if_necessary(g0)

        play.print_gameboard(gb)

        assert gb[0].shape == (5, 5)
        assert gb[1] == (1, 1)
    

    def test_expand_north(self):
        g0 = play.create_configuration(rows = 3, cols = 3)
        g0[0][0,1] = True
        play.print_gameboard(g0)
        gb = gam.expand_gameboard_if_necessary(g0)

        play.print_gameboard(gb)

        assert gb[0].shape == (4, 3)
        assert gb[1] == (1, 0)

    def test_cutoff(self):
        g0 = play.create_configuration(rows = 3, cols = 3)
        g0[0][0,1] = True
        g0[0][1,1] = True
        g0[0][1,2] = True
        
        play.print_gameboard(g0)
        gb = gam.get_base_configuration(g0)

        play.print_gameboard(gb)

        assert gb[0].shape == (2, 2)
        assert gb[1] == (0, -1)

    def test_origin(self):
        g0 = play.create_configuration(rows = 3, cols = 4)
        assert g0[1] == (0, 0)

        g1 = play.create_configuration(rows = 3, cols = 4, origin = (1, 2))
        
        assert g0[1] == (0, 0)
        assert g1[1] == (1, 2)

        g1[0][1, 1] = 1

        g1 = gam.get_base_configuration(g1)
        assert g1[1] == (0, 1)


    def test_get_neighbors(self):
        g0 = play.create_configuration(rows = 3, cols = 3)
        g0[0][0,0] = True
        g0[0][0,2] = True
        g0[0][2,2] = True
        play.print_gameboard(g0)
        nc = play.get_neighbour_count(g0)
        print(nc)