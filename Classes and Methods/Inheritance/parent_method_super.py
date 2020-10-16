class Person():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def speak(self):
        print('Hello! My name is %s' % self.first_name)

# Создадим подкласс person, который сможет говорить больше, чем в методе speak
# Унаследуем метод speak с фразой 'Hello! My name is ...' с помощью super()

class TalkativePerson(Person):

    def speak(self):
        super().speak()
        print('Nice to meet u!')

john = TalkativePerson('John', 'Snow')
john.speak()