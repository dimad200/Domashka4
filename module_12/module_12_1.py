import unittest

import runner_and_tournament
from module_12.runner_and_tournament import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        mister_begun_1=Runner("Магамет")
        # print(mister_begun_1.name)
        i=0
        while i <10:
            mister_begun_1.walk()
            i+=1
        self.assertEqual(mister_begun_1.distance,50)

    def test_run(self):
        mister_begun_2 = Runner("Ахмед")
        i = 0
        while i < 10:
            mister_begun_2.run()
            i += 1
        self.assertEqual(mister_begun_2.distance, 100)

    def test_challenge(self):
        mister_begun_1 = Runner("Магамет")
        mister_begun_2 = Runner("Ахмед")
        i = 0
        while i < 10:
            mister_begun_1.run()
            mister_begun_2.walk()
            i += 1
        self.assertNotEqual(mister_begun_1.distance,mister_begun_2.distance)






