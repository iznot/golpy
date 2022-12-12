
import numpy as np
import run_simulation as sim
import samples as samp
import unittest
import basic_game_functions as gm
import gameboard_manipulation as gam

class TestSimulation(unittest.TestCase):

    def test_check_exit_criteria_stable(self):
        gleiter = samp.get_gleiter()
        gameboards = [gleiter, gleiter]
        res, p = sim.check_exit_criteria(gameboards)
        assert res == 'stable'

    

    def test_check_exists(self):
        gameboards = [samp.get_Eater(), samp.get_erased(), samp.get_gleiter()]
        gameboard_to_check = samp.get_Tuemmler()
        res1, i = sim.check_exists(gameboard_to_check, gameboards)
        assert res1 == False
        assert i == -1


    def test_check_not_exists(self):
        gameboards = [samp.get_Eater(), samp.get_Tuemmler(), samp.get_erased(), samp.get_gleiter()]
        gameboard_to_check = samp.get_Tuemmler()
        res1, i = sim.check_exists(gameboard_to_check, gameboards)
        assert res1 == True
        assert i == 4


    def test_pulsator_oscilator(self):
        gameboard = samp.get_pulsator()
        gameboards = [gameboard]
        for i in range(20):
            gameboard_new = gm.play(gameboard)
            list.append(gameboards, gameboard_new)
            gameboard = gameboard_new
        
        exit_criteria, periodicity = sim.check_exit_criteria(gameboards)

        assert exit_criteria == 'oscilator'
        assert periodicity == 15

    def test_gleiter_spaceship(self):
        gameboard = samp.get_gleiter()
        gameboards = [gameboard]
        for i in range (7):
            gameboard_new = gm.play(gameboard)
            list.append(gameboards, gameboard_new)
            gameboard = gameboard_new
        
        exit_criteria, periodicity = sim.check_exit_criteria(gameboards)

        assert exit_criteria == 'spaceship'
        assert periodicity == 4


        gameboard = samp.get_gleiter()
        gameboards = [gameboard]
        for i in range (7):
            gameboard_new = gm.play(gameboard)
            list.append(gameboards, gameboard_new)
            gameboard = gameboard_new
        
        exit_criteria, periodicity = sim.check_exit_criteria(gameboards)

        assert exit_criteria == 'spaceship'
        assert periodicity == 4

    def test_oscillator(self):
        gameboard = sim.convert_to_gameboard('5,19,0x2f')
        gameboards, exit_criteria, periodicity, i = sim.run_simulation(gameboard,100)
        assert exit_criteria == 'oscilator'
        assert periodicity == 2
        assert i == len(gameboards)

    def test_run_simulation(self):
        gameboard = samp.get_gleiter()
        gameboards, exit_criteria, periodicity = sim.run_simulation(gameboard, 30)
        assert len(gameboards) >= periodicity
        assert exit_criteria == 'spaceship'
        assert periodicity == 4
    
    def test_convert_to_string(self):
        g0 = gm.create_gameboard(rows = 3, cols = 3)
        g0[0,0] = True
        g0[0,2] = True
        g0[2,2] = True
        res = sim.convert_to_string(g0)
        assert res == '3,0,0x141'
        res_list = res.split(',')
        width = res_list[0]
        leading_zeros = res_list[1]
        gameboard_number = res_list[2]
        assert type(res) is str
        assert width == '3'
        assert leading_zeros == '0'
        assert gameboard_number == '0x141'

    def test_convert_to_string_2(self):
        g0 = gm.create_gameboard(rows = 12, cols = 12)
        g0[1,1] = True
        g0[1,3] = True
        g0[3,3] = True
        res = sim.convert_to_string(g0)
        assert res == '12,13,0x500000100000000000000000000000000'
    
    def test_convert_to_gameboard(self):
        gb_str = '6,13,0x530ebd1009000a0000000000000000000'
        gb = sim.convert_to_gameboard(gb_str)
        columns = gb.shape[1]
        assert columns == 6
        assert gb.sum() == 18
        gb_str_2 = sim.convert_to_string(gb)
        assert gb_str_2 == gb_str
        
    def test_convert_huge_gameboard(self):
        g0 = gm.create_gameboard(rows = 1000, cols = 900)
        g0[1,1] = True
        g0[1,3] = True
        g0[3,3] = True
        res = sim.convert_to_string(g0)
        gb = sim.convert_to_gameboard(res)
        assert gm.gameboard_equal(gb, g0)
    
    def test_new_cut(self):
        gb = sim.convert_to_gameboard('5,19,0x2f')
        gb = gam.cut_both_axis(gb)
