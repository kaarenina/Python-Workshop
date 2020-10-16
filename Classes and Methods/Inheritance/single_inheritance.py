
class Pet():

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

class Cat(Pet):
    is_feline = True

class Dog(Pet):
    is_feline = False

# Check

my_cat = Cat('Vasya', 8)
print(my_cat.name)