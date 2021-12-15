import unittest
from Math import Math

class TestMath(unittest.TestCase):
    def test_init(self):
        math = Math(10, 5)
        self.assertEqual(math.a, 10)
        self.assertEqual(math.b, 5)

    def test_add(self):
        math = Math(10, 5)
        self. assertEqual(math.addition(), 15)

    def test_multi(self):
        math = Math(10, 5)
        self. assertEqual(math.multiplication(), 50)

    def test_div(self):
        math = Math(10, 5)
        self. assertEqual(math.division(), 2)

    def test_sub(self):
        math = Math(10, 5)
        self. assertEqual(math.substaction(), 5)


if __name__ == '__main__':
    unittest.main()


# class TestCubes(unittest.TestCase):
#
#     def test_val(self):
#         x = My_math (5,2)
#         self.assertEqual(x.a, 5)
#         self.assertEqual(x.b, 2)
#
#     def test_operation_sub(self):
#         x = My_math(5,2)
#         self.assertEqual(x.subtraction(),2)
#
#     def test_operation_add(self):
#         x = My_math(5, 2)
#         self.assertEqual(x.addition(), 7)
#
#     def test_operation_div(self):
#         x = My_math(5, 2)
#         self.assertEqual(x.division(), 2.5)
#
#     def test_operation_mul(self):
#         x = My_math(5, 2)
#         self.assertEqual(x.multiplication(), 10)