import unittest


def sum_numers(x, y):
    return x + y


class TestSumNumers(unittest.TestCase):
    def test_sum_numers(self):
        result = sum_numers(x = 2, y = 3)
        self.assertEqual(result, second = 5)


def diff_numers(x, y):
    return x - y


class TestDiffNumers(unittest.TestCase):
    def test_diff_numers(self):
        result = diff_numers(x = 5, y = 1)
        self.assertEqual(result, second = 4)



def abs_num(x):
    return abs(x)


class TestAbsNum(unittest.TestCase):
    def test_abs_num(self):
        result = abs_num(x = -5)
        self.assertEqual(result, second = 5)


def comp_numbers(x, y):
    return x * y


class TestCompNumbers(unittest.TestCase):
    def test_comp_numbers(self):
        result = comp_numbers(x = -5, y = 0)
        self.assertEqual(result, second = 0)


def square_num(x):
    return x ** 0.5


class TestSquareNum(unittest.TestCase):
    def test_square_num(self):
        result = square_num(x = 9)
        self.assertEqual(result, second = 3)


def div_numbers(x, y):
    if y == 0:
        raise ValueError('Деление на ноль!')
    return x / y


class TestDivNumbers(unittest.TestCase):
    def test_div_numbers(self):
        with self.assertRaises(ValueError):
            div_numbers(x = -5, y = 0)         
        result = div_numbers(x = 8, y = 2)
        self.assertEqual(result, second = 5)
        


if __name__ == '__main__':
    unittest.main()