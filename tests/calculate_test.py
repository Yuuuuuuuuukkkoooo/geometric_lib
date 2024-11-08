import unittest
from calculate import calc  # Импортируем функцию calc из модуля calculate


class TestCalc(unittest.TestCase):

    def test_circle_perimeter(self):
        fig = 'circle'
        func = 'perimeter'
        size = [5]
        result = calc(fig, func, size)
        self.assertAlmostEqual(result, 31.4159, places=4)

    def test_circle_area(self):
        fig = 'circle'
        func = 'area'
        size = [5]
        result = calc(fig, func, size)
        self.assertAlmostEqual(result, 78.5398, places=4)

    def test_square_perimeter(self):
        fig = 'square'
        func = 'perimeter'
        size = [4]
        result = calc(fig, func, size)
        self.assertEqual(result, 16)

    def test_square_area(self):
        fig = 'square'
        func = 'area'
        size = [4]
        result = calc(fig, func, size)
        self.assertEqual(result, 16)

    def test_invalid_figure(self):
        fig = 'triangle'
        func = 'area'
        size = [5, 5, 5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_function(self):
        fig = 'circle'
        func = 'volume'
        size = [5]
        with self.assertRaises(AssertionError):
            calc(fig, func, size)

    def test_invalid_size_parameter(self):
        fig = 'square'
        func = 'area'
        size = ['invalid_size']
        with self.assertRaises(TypeError):
            calc(fig, func, size)


if __name__ == "__main__":
    unittest.main()
