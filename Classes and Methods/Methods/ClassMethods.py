'''
Class Methods are like instance methods, except that instead of the instance of an object
being passed as the first positional self argument, the class itself is passed as the first argument.
As with static methods, you use a decorator to designate a class method.
'''

class Australian():
    is_human = True
    enjoys_sport = True

    @classmethod
    def is_sporty_human(cls):
        return  cls.is_human and cls.enjoys_sport

# You can call this method on the class item
print(Australian.is_sporty_human())

# Как вариант, мы можем вызвать метод экземпляра
aussie = Australian()
aussie.is_sporty_human()

# Также методы класса можно использовать как хорошую утилиту для создания новых методов
# Например:

class Country():

    def __init__(self, name='Unspecified', population=None, size_kmsq=None):
        self.name = name
        self.population = population
        self.size_kmsq = size_kmsq

    '''  
    Теперь предположим, что вы хотите избежать ситуации, когда пользователь указывает 
    размер в квадратных милях, а не квадратных километрах.
    Вы можете использовать метод класса, который принимает от пользователя квадратную мили,
    преобразуя ее в квадратные километры, прежде чем инициализировать экземпляр класса.
    '''
    @classmethod
    def create_with_msq(cls, name, population, size_msq):
        size_kmsq = size_msq / 0.621371 ** 2
        return cls(name, population, size_kmsq)

mexico = Country.create_with_msq('Mexico', 150e6, 760000)
print(mexico.size_kmsq)