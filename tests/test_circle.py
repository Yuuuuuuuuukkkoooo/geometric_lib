import unittest

from circle import area, perimeter


class TestCircle(unittest.TestCase):
    def test_circle_area_1(self):
        r = 5
        result = area(r)
        self.assertAlmostEqual(result, 78.53981633974483, places=5)

    def test_circle_perimeter_1(self):
        r = 5
        result = perimeter(r)
        self.assertAlmostEqual(result, 31.41592653589793, places=5)

    def test_circle_area_2(self):
        r = 439140
        result = area(r)
        self.assertAlmostEqual(result, 605837103936.6738, places=5)

    def test_circle_perimeter_2(self):
        r = 439140
        result = perimeter(r)
        self.assertAlmostEqual(result, 2759197.9957948434, places=5)

    def test_circle_area_3(self):
        r = 4.5
        result = area(r)
        self.assertAlmostEqual(result, 63.61725123519331, places=5)

    def test_circle_perimeter_3(self):
        r = 4.5
        result = perimeter(r)
        self.assertAlmostEqual(result, 28.274333882308138, places=5)

    def test_invalid_parameters(self):
        # Negative test for invalid inputs
        with self.assertRaises(TypeError):
            area("invalid")

        with self.assertRaises(TypeError):
            perimeter("invalid")


if __name__ == "__main__":
    unittest.main()
