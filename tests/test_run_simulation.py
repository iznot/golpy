
import numpy as np
import run_simulation as sim
import samples as samp
import unittest
import basic_game_functions as gm

class TestSimulation(unittest.TestCase):

    def test_check_exit_criteria_stable(self):
        gleiter = samp.get_gleiter()
        gameboards = [gleiter, gleiter]
        res = sim.check_exit_criteria(gameboards)
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