
import numpy as np
import run_simulation as sim
import samples as samp
import unittest

class TestSimulation(unittest.TestCase):

    def test_check_exit_criteria_stable(self):
        gleiter = samp.get_gleiter()
        gameboards = [gleiter, gleiter]
        res = sim.check_exit_criteria(gameboards)
        assert res == 'stable'