class Temperature():
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

if __name__ == '__main__':
    freezing = Temperature(0)
    print(freezing.fahrenheit, freezing.celsius)