import unittest

from triangle import area, perimeter


class TestTriangle(unittest.TestCase):
    def test_triangle_area_1(self):
        a, h = 5, 10
        result = area(a, h)
        self.assertEqual(result, 25.0)

    def test_triangle_perimeter_1(self):
        a, b, c = 3, 4, 5
        result = perimeter(a, b, c)
        self.assertEqual(result, 12)

    def test_triangle_area_2(self):
        a, h = 512, 10341
        result = area(a, h)
        self.assertEqual(result, 2647296.0)

    def test_triangle_perimeter_2(self):
        a, b, c = 3123, 4312, 7781
        result = perimeter(a, b, c)
        self.assertEqual(result, 15216)

    def test_triangle_area_3(self):
        a, h = 52.12, 10.1
        result = area(a, h)
        self.assertEqual(result, 263.20599999999996)

    def test_triangle_perimeter_3(self):
        a, b, c = 3.1, 4.3, 5.8
        result = perimeter(a, b, c)
        self.assertEqual(result, 13.2)

    def test_invalid_parameters(self):
        with self.assertRaises(TypeError):
            area("invalid")

        with self.assertRaises(TypeError):
            perimeter("invalid")


if __name__ == "__main__":
    unittest.main()
