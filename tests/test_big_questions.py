import unittest

import manipulation as gam
import play
import big_questions as big


class TestBigQuestions(unittest.TestCase):


#print_configuration

    def test_is_contained(self):
        config_str = "(30, 30):(0, 0)|(3, 3):1:0x8f"
        config = gam.create_configuration_from_string(config_str)
        config_to_compare_str = "(3, 3):(0, 0)|(3, 3):0:0x11e"
        config_to_compare = gam.create_configuration_from_string(config_to_compare_str)
        res = big.is_contained(config, config_to_compare)
        assert res == True


    def test_is_not_contained(self):
        config_str = "(30, 30):(0, 0)|(3, 3):1:0x8f"
        config = gam.create_configuration_from_string(config_str)
        config_to_compare_str = "(3, 3):(0, 0)|(3, 3):0:0x11f"
        config_to_compare = gam.create_configuration_from_string(config_to_compare_str)
        res = big.is_contained(config, config_to_compare)
        assert res == False