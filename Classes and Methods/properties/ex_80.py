
class Temperature():
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):
        return self.celsius * 9 / 5 + 32

    '''
    Add a @fahrenheit.setter function that converts the fahrenheit value to Celsius 
    and stores it in the celsius instance method 
    '''
    @fahrenheit.setter
    def fahrenheit(self, value):
        if value < -460:
            raise ValueError('Temperature less than -460F are not possible')
        self.celsius = (value - 32) * 5 / 9

# Create a temperature and check the fahrenheit property
temp = Temperature(5)
print(temp.fahrenheit)

# Update the fahrenheit property and check the celsius attribute
temp.fahrenheit = -454
print(temp.celsius)