class Person():

     def __init__(self, name):
         self.name = name


class Baby(Person):

    def speak(self):
        print('Blah blah blah')

class Adult(Person):

    def speak(self):
        print('Hello, my name is %s' % self.name)

vanya = Baby('Ivan')
anya = Adult('Anna')

vanya.speak()
anya.speak()