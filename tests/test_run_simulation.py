
import numpy as np
import run_simulation as sim
import samples as samp
import unittest
import basic_game_functions as gm

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

    def test_run_simulation(self):
        gameboard = samp.get_gleiter()
        gameboards, exit_criteria, periodicity = sim.run_simulation(gameboard, 10)
        assert len(gameboards) >= periodicity
        assert exit_criteria == 'spaceship'
        assert periodicity == 4
    
    def test_convert_to_string(self):
        g0 = gm.create_gameboard(rows = 3, cols = 3)
        g0[0,0] = True
        g0[0,2] = True
        g0[2,2] = True
        res = sim.convert_to_string(g0)
        assert res == '3,0,321'
        res_list = res.split(',')
        width = res_list[0]
        leading_zeros = res_list[1]
        gameboard_number = res_list[2]
        assert type(res) is str
        assert width == '3'
        assert leading_zeros == '0'
        assert gameboard_number == '321'
