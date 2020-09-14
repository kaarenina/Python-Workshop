import datetime

'''
Таким образом, статические методы прикреплены к классу лишь для удобства 
и не могут менять состояние ни класса, ни его экземпляра.
'''

# Create a simple Diary class that stores two dates
class Diary():
    def __init__(self, birthday, new_year):
        self.birhday = birthday
        self.newYear = new_year

    @staticmethod
    def format_date(date):
        return date.strftime('%d-%b-%y')

    # Add two instance methods that print out dates in dd-mm-yy format
    def show_birthday(self):
        return self.format_date(self.birhday)

    def show_newYear(self):
        return self.format_date(self.newYear)

# Create a new Diary object and test one of the methods
my_diary = Diary(datetime.date(2020, 10, 20), datetime.date(2020, 12, 31))
print(my_diary.show_newYear())

'''
Представим, что у нас таких дат множество. Тогда строчка кода strftime('%d-%b-%y') будет встречаться очень часто.
И предположим, что нам потребовалось сменить формат даты. Тогда нам прийдется менять код во многих местах
Конечно, мы можем создать format_date статический метод для хранения этой логики всего раз
'''
