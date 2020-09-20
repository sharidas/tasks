"""
This module has the test for our minimum coins problem
"""

import unittest
import min_coins

class MinCoinsTest(unittest.TestCase):
    """
    Class MinCoinsTest has the methods to test our
    minimum coins problem
    """

    def test_no_return(self):
        """
        Test for no coins to be returned as balance
        """
        expected_output = {}

        result = min_coins.return_coins(2, 2)

        assert result == expected_output

    def test_get_small_balance(self):
        """
        Test for small balance amount
        """

        expected_output = {10: 1, 50:1}

        result = min_coins.return_coins(2.4, 3)

        assert expected_output == result

        expected_output = {5 : 1, 10 : 1, 20 : 1}

        result = min_coins.return_coins(1.65, 2)

        assert expected_output == result

    def test_big_balance(self):
        """
        Test for large balance amount.
        Say for example the return is 600 we return 3 coins of 2 euros
        """

        expected_output = {200: 3}

        result = min_coins.return_coins(1, 7)

        assert expected_output == result

        expected_output = {5: 1, 20: 1, 100 : 1, 200 : 3}
        result = min_coins.return_coins(0.75, 8)

        assert expected_output == result

    def test_negative_balance(self):
        """
        Test for negative balance!!
        """

        expected_output = {}
        result = min_coins.return_coins(3.4, 3)

        assert expected_output == result
