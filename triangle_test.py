import unittest
from triugla import TriangleChecker


class Test_TriangleChecker(unittest.TestCase):

    def test_init(self):
        triangle = TriangleChecker(5, 3, 10)
        self.assertEqual(triangle.a, 5)
        self.assertEqual(triangle.b, 3)
        self.assertEqual(triangle.c, 10)

    def test_wrong_values(self):
       triangle = TriangleChecker('length',  (1, 2, 3), {4: 5})
       self.assertEqual(triangle.is_triangle(),'Введены не числа')

    def test_negative_numbers(self):
       triangle = TriangleChecker(-16,11,14)
       self.assertEqual(triangle.is_triangle(),'Нельзя построть треугольник с негативными числами!')

    def test_triangle_not_exist(self):
       triangle = TriangleChecker(166,21,44)
       self.assertEqual(triangle.is_triangle(),'Нельзя построть треугольник с этими сторонами!')


    def test_triangle_exist(self):
       triangle = TriangleChecker(16,21,34)
       self.assertEqual(triangle.is_triangle(),'Ура! Треугольник можно построить!')

    if __name__ == "__main__":
        unittest.main()
