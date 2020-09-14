# The property decorator

class Temperature():
    def __init__(self, celsium):
        self.celsium = celsium

    @property
    def fahrenheit(self):
        return self.celsium * 9 / 5 + 32

my_temp = Temperature(100)
print(my_temp.fahrenheit)