class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    @full_name.setter
    def full_name(self, name):
        first, last = name.split(' ')
        self.first_name = first
        self.last_name = last

my_person = Person('Alexey', 'Vronsky')
my_person.full_name = 'Alexey Karenin' # Принимает людей у которых только два слова

class BetterPerson(Person):

    @property
    def full_name(self):
        return '%s %s' % (self.first_name, self.last_name)
    
    @full_name.setter
    def full_name(self, name):
        names = name.split(' ')
        self.first_name == names[0]
        if len(names) > 2:
            self.last_name = ' '.join(names[1:])
        elif len(names) == 2:
            self.last_name = names[1]
        else:
            raise NameError('wrong name')

my_better_person = BetterPerson('Alexey', 'Vronsky')
my_better_person.full_name = 'Alex Karenin Vronsky'
print(my_better_person.first_name)
print(my_better_person.last_name)
