import datetime

class MyDate(datetime.date):

    '''
    Метод, который использует timedelta, чтобы увеличить дату
    '''
    def add_days(self, n):
        return self + datetime.timedelta(n)

d = MyDate(2020, 4, 3)
print(d.add_days(2))
print(d.add_days(365))