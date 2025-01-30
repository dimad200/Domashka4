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

    def test_1(self):
        test_ = Tournament(90, self.runer_1, self.runer_3)
        itog = test_.start()
        max_key = 0

        for i in itog.keys():
            max_key = (int(i) if max_key < int(i) else max_key)
        self.assertTrue(itog[max_key] == "Ник")

        RunnerTest.all_results["test_1"] = itog


    def test_2(self):
        test_ = Tournament(90, self.runer_2, self.runer_3)
        itog = test_.start()
        max_key = 0
        for i in itog.keys():
            max_key = (int(i) if max_key < int(i) else max_key)
        self.assertTrue(itog[max_key] == "Ник")

        RunnerTest.all_results["test_2"] = itog

    def test_3(self):
        test_ = Tournament(90, self.runer_1, self.runer_2, self.runer_3)
        itog = test_.start()
        max_key = 0
        for i in itog.keys():
            max_key = (int(i) if max_key < int(i) else max_key)
        self.assertTrue(itog[max_key] == "Ник")
        RunnerTest.all_results["test_3"] = itog

    @classmethod

    def tearDownClass(cls):

        for i in cls.all_results.keys():
            # print(cls.all_results[i])
            for k in cls.all_results[i]:
                print(f"{k}: {cls.all_results[i][k].name}", end=" ")
            print("",end="\n")



