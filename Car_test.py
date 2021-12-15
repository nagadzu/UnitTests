import unittest
from Car import Car

class TestCar(unittest.TestCase):

    def test_start_car(self):
        car = Car('белый жемчуг', 'хетчбэк', 2000)
        self.assertEqual(car.start_car(), 'Автомобиль заведен')

    def test_stop_car(self):
        car = Car('белый жемчуг', 'хетчбэк', 2000)
        self.assertEqual(car.stop_car(), 'Автомобиль заглушен')

    def test_car_year(self):
        car = Car('белый жемчуг', 'хетчбэк', 2000)
        self.assertEqual(car.car_year(), f'Год выпуска: {car.year}')

    def test_car_type(self):
        car = Car('белый жемчуг', 'хетчбэк', 2000)
        self.assertEqual(car.car_type(), f'Тип кузова: {car.type}')

    def test_color(self):
        car = Car('белый жемчуг', 'хетчбэк', 2000)
        self.assertEqual(car.car_color(), f'Цвет: {car.color}')



if __name__ == '__main__':
    unittest.main()