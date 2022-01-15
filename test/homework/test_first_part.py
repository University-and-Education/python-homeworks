import unittest

from src.homework import first_part


class TestFirstHomeWork(unittest.TestCase):

    def test_homework_first(self):
        input_list = ['abc', '11', ' ']
        self.assertEqual(len(first_part.homework_first(input_list)), 2)
        self.assertEqual(first_part.homework_first(input_list).pop(1), '11')

    def test_homework_second(self):
        self.assertEqual(first_part.homework_second(5), 'Весна')
        self.assertEqual(first_part.homework_second(12), 'Зима')
        self.assertEqual(first_part.homework_second(8), 'Лето')
        self.assertEqual(first_part.homework_second(22), ValueError)

    def test_homework_third(self):
        self.assertEqual(first_part.homework_third(-1), ValueError)
        self.assertEqual(first_part.homework_third(3), '1 1 2')

    def test_homework_fourth(self):
        input_list = ['abc', '11', 'abc', 'abc', '11', 'arthur', '0']
        empty_list = []
        self.assertEqual(first_part.homework_fourth(input_list).get('abc'), 3)
        self.assertEqual(first_part.homework_fourth(input_list).get('11'), 2)
        self.assertEqual(first_part.homework_fourth(input_list).get('arthur'), 1)
        self.assertEqual(first_part.homework_fourth(empty_list).get('2'), None)

    def test_homework_fifth(self):
        first_input_list = [5, 2, 2]
        second_input_list = [4, 3, 5]
        self.assertEqual(first_part.homework_fifth(first_input_list), 3)
        self.assertEqual(first_part.homework_fifth(second_input_list), 4)

    def test_homework_sixth(self):
        self.assertEqual(first_part.homework_sixth(11), True)
        self.assertEqual(first_part.homework_sixth(2), True)
        self.assertEqual(first_part.homework_sixth(160), False)
        self.assertEqual(first_part.homework_sixth(12), False)

    def test_homework_seventh(self):
        input_list = ['abc', '11', 'abc', 'abc', '11', 'arthur', '0']
        self.assertEqual(first_part.homework_seventh(input_list).pop(0), 'arthur')
        self.assertEqual(first_part.homework_seventh(input_list).pop(1), 'abc')


