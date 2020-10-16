import datetime


class Diary:

    def __init__(self, birthday, christmas):
        self.birthday = birthday
        self.christmas = christmas

    @staticmethod
    def format_date(date):
        return date.strftime('%d-%m-%y')

    def show_birthday(self):
        return self.format_date(self.birthday)

    def show_christmas(self):
        return self.format_date(self.christmas)


# Предположим, что нам нужно создать класс, который бы выводил другой формат дат, который захочет пользователь
class CustomDiary(Diary):

    def __init__(self, birthday, christmas, date_format):
        self.date_format = date_format
        super().__init__(birthday, christmas)

    def format_date(self, date):
        return date.strftime(self.date_format)


first_diary = CustomDiary(datetime.date(2019, 1, 1), datetime.date(2019, 7, 10), '%d-%b-%Y')
second_diary = CustomDiary(datetime.date(2019, 10, 20), datetime.date(2019, 1, 1), '%d/%m/%Y')
print(first_diary.show_birthday())
print(second_diary.show_christmas())
