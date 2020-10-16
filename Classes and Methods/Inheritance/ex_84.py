# Multiple inheritance
import datetime

class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Baby(Person):

    def speak(self):
        print('Blah blah blah')


class Adult(Person):

    def speak(self):
        print('Hello, my name is %s' % self.first_name)

# Создадим класс Calendar, который поможет стать детям организованными
class Calendar():

    def book_apploinment(self, date):
        print('Booking appointment for date %s' % date)

# Создадим OrganizedBaby и OrganizedAdult, которые наследуюются от нескольких классов
class OrganizedAdult(Adult, Calendar):
    pass

class OrganizedBaby(Baby, Calendar):

    # Переопределим метод book_apploinment с помощью метода super()
    def book_apploinment(self, date):
        print('Note that you are booking an appointment with a baby.')
        super().book_apploinment(date)



ivan = OrganizedAdult('Ivan', 'Ivanov')
boris = OrganizedBaby('Boris', 'Petrov')
ivan.speak()
boris.speak()
boris.book_apploinment(datetime.date(2018,1,1))
