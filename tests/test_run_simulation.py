

import unittest

import game
import manipulation as gam
import play
import samples as samp
import simulation as sim


class TestSimulation(unittest.TestCase):

    def test_check_exit_criteria_stable(self):
        gleiter = samp.get_gleiter()
        configurations = [gleiter, gleiter]
        res, p = game.check_exit_criteria(configurations)
        assert res == 'stable'

    

    def test_check_exists(self):
        configurations = [samp.get_Eater(), samp.get_erased(), samp.get_gleiter()]
        configuration_to_check = samp.get_Tuemmler()
        res1, i = game._check_exists(configuration_to_check, configurations, True)
        assert res1 == False
        assert i == -1


    def test_check_not_exists(self):
        configurations = [samp.get_Eater(), samp.get_Tuemmler(), samp.get_erased(), samp.get_gleiter()]
        configuration_to_check = samp.get_Tuemmler()
        res1, periodicity = game._check_exists(configuration_to_check, configurations, True)
        assert res1 == True
        assert periodicity == 3


    def test_pulsator_oscilator(self):
        configuration = samp.get_pulsator()
        configurations = [configuration]
        for i in range(20):
            configuration_new = play.play(configuration)
            list.append(configurations, configuration_new)
            configuration = configuration_new
        
        exit_criteria, periodicity = game.check_exit_criteria(configurations)

        assert exit_criteria == 'oscillator'
        assert periodicity == 15

    def test_gleiter_spaceship(self):
        configuration = samp.get_gleiter()
        configurations = [configuration]
        for i in range (7):
            configuration_new = gam.expand_gameboard_if_necessary(configuration)
            configuration_new = play.play(configuration_new)
            configuration_new = gam.get_base_configuration( configuration_new )
            list.append(configurations, configuration_new)
            configuration = configuration_new
        
        exit_criteria, periodicity = game.check_exit_criteria(configurations)

        assert exit_criteria == 'spaceship'
        assert periodicity == 4


    def test_oscillator(self):
        configuration = gam.create_configuration_from_string('(20, 20):(9, 8)|(2, 4):0:0x8f')
        configurations, exit_criteria, periodicity, i = game.play_full_game(configuration,100)
        assert exit_criteria == 'oscillator'
        assert periodicity == 2
        assert i == len(configurations)-1


    def test_run_simulation(self):
        configuration = samp.get_gleiter()
        configurations, exit_criteria, periodicity, i = game.play_full_game(configuration, 30)
        assert len(configurations) >= periodicity
        assert exit_criteria == 'spaceship'
        assert periodicity == 4
    
    def test_convert_to_string(self):
        g0 = play.create_configuration(rows = 5, cols = 4, origin=(-12, -15))
        g0[0][1,0] = True
        g0[0][1,2] = True
        g0[0][2,1] = True
        res = gam.convert_to_string_representation(g0)
        assert res == '(5, 4):(1, 0)|(2, 3):0:0x2a'
        g1 = gam.create_configuration_from_string(res)
        assert gam.configuration_equal(g0, g1, check_origin=False)

    


    def test_convert_to_string_2(self):
        g0 = play.create_configuration(rows = 12, cols = 12)
        g0[0][1,1] = True
        g0[0][1,3] = True
        g0[0][3,3] = True
        res = gam.convert_to_string_representation(g0)
        assert res == '(12, 12):(1, 1)|(3, 3):0:0x141'
    
    def test_convert_to_configuration(self):
        gb_str = '(12, 12):(2, 3)|(7, 8):4:0x8a8002810a825'
        gb = gam.create_configuration_from_string(gb_str)
        columns = gb[0].shape[1]
        assert columns == 12
        gb_str_2 = gam.convert_to_string_representation(gb)
        assert gb_str_2 == gb_str
        
    def test_convert_huge_configuration(self):
        g0 = play.create_configuration(rows = 1000, cols = 900)
        g0[0][1,1] = True
        g0[0][1,3] = True
        g0[0][3,3] = True
        res = gam.convert_to_string_representation(g0)
        gb = gam.create_configuration_from_string(res)
        assert gam.configuration_equal(gb, g0)
    
    def test_new_cut(self):
        gb = gam.create_configuration_from_string('(12, 12):(2, 3)|(10, 8):4:0x8a8002810a825202020')
        gb = gam.get_base_configuration(gb)
        gb_str = gam.convert_to_string_representation(gb)
        print(gb_str)
        assert gb_str == "(10, 8):(0, 0)|(10, 8):4:0x8a8002810a825202020"



