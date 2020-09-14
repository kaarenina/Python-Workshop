# Static methods are similar to instance methods,
# except that they do not implicitly pass the positional self argument.

class Pet():
    def __init__(self, height):
        self.height = height

    is_human = False
    owner= 'Michael Smith'

    @staticmethod
    def owned_by_smith_family():
        return 'Smith' in Pet.owner

nibbles = Pet(100)
print(nibbles.owned_by_smith_family())