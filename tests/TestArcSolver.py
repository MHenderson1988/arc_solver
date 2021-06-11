from unittest import TestCase

import numpy as np

from main.ArcSolver import ArcSolver, convert_y_values

class TestArcSolver(TestCase):
    def test_calc_start_angle(self):
        test = ArcSolver(1, 1)
        print(test.calc_start_angle())