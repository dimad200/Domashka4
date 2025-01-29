import unittest

from runner_and_tournament import *


class RunnerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runer_1 = Runner("Усэйн", 10)
        self.runer_2 = Runner("Андрей", 9)
        self.runer_3 = Runner("Ник", 3)


    @classmethod
    def tearDownClass(cls):
        print(cls.all_results)

    def test_1(self):
        t_1 = Tournament(90, self.runer_1, self.runer_2)
        result= t_1.start()
        print(result)
        for i in result:
