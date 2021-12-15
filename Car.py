class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    @staticmethod
    def start_car():
        return f'Автомобиль заведен'

    @staticmethod
    def stop_car():
        return f'Автомобиль заглушен'

    def car_year(self):
        return f'Год выпуска: {self.year}'

    def car_type(self):
        return f'Тип кузова: {self.type}'

    def car_color(self):
        return f'Цвет: {self.color}'

car = Car('белый жемчуг', 'хетчбэк', 2000)

print(Car.start_car())
print(Car.stop_car())
print(car.car_year())
print(car.car_type())
print(car.car_color())
