class Temperature():
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < -460:
            raise ValueError('Temperatures less than -460F are not possible')
        self.celsius = (value - 32) * 5 / 9


if __name__ == '__main__':
    t = Temperature(0)
    print(t.fahrenheit, t.celsius)
    t.fahrenheit = 0
    print(t.fahrenheit, t.celsius)
    t.fahrenheit = -40
    print(t.fahrenheit, t.celsius)
    t.fahrenheit = -500
