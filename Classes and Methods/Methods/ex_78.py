import random

'''
Методы класса могут менять состояние класса, что отразится на всех объектах этого класса,
но не могут менять конкретный объект.
'''
class Pet():

    def __init__(self, height):
        self.height = height

    is_human = False
    owner = 'Michael Ivanov'

    # Добавим метод класса, который возвращает принадлежит ли питомец семье Ивановых
    @classmethod
    def owned_by_ivanov_family(cls):
        return 'Ivanov' in cls.owner

    # Добавим метод класса, который генерирует случайное число и назначает его высотой питомца
    @classmethod
    def create_random_height_pet(cls):
        height = random.randrange(0, 100)
        return cls(height)

for i in range(5):
    pet = Pet.create_random_height_pet()
    print(pet.height)