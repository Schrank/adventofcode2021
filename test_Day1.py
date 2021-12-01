import unittest

from Day1 import Day1


class TestDay1(unittest.TestCase):

    def test_count(self):
        day1 = Day1()
        depths = "1\n2\n3"
        self.assertEqual(day1.count(depths), 2)
    pass

    def test_countTwo(self):
        day1 = Day1()
        depths = '199\n200\n208\n210\n200\n207\n240\n269\n260\n263'
        self.assertEqual(day1.count2(depths), 5)

