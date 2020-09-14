# Create a Person class with two instance attributes, the first and last name

class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    # Add a full_name property with the @property decorator
    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    # Add a full_name setter
    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

# Create a customer object and test the full_name property
customer = Person('NATASHA', 'ROSTOVA')
print(customer.full_name)
customer.full_name = 'SONYA ROSTOVA'
print(customer.full_name)