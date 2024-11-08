import unittest

from square import area, perimeter


class TestSquare(unittest.TestCase):
    def test_square_area_1(self):
        a = 4
        result = area(a)
        self.assertEqual(result, 16)

    def test_square_perimeter_1(self):
        a = 4
        result = perimeter(a)
        self.assertEqual(result, 16)

    def test_square_area_2(self):
        a = 483819
        result = area(a)
        self.assertEqual(result, 234080824761)

    def test_square_perimeter_2(self):
        a = 483819
        result = perimeter(a)
        self.assertEqual(result, 1935276)

    def test_square_area_3(self):
        a = 16.23
        result = area(a)
        self.assertEqual(result, 263.41290000000004)

    def test_square_perimeter_3(self):
        a = 16.23
        result = perimeter(a)
        self.assertEqual(result, 64.92)

    def test_invalid_parameters(self):
        with self.assertRaises(TypeError):
            area("invalid")

        with self.assertRaises(TypeError):
            perimeter("invalid")


if __name__ == "__main__":
    unittest.main()
