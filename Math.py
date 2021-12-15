class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a // self.b

    def substaction(self):
        return self.a - self.b


math = Math(a=10, b=5)
print(math.addition())
print(math.multiplication())
print(math.division())
print(math.substaction())

