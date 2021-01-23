import datetime


class MyDate(datetime.date):
    def add_days(self, n):
        return self + datetime.timedelta(n)


if __name__ == '__main__':
    d = MyDate(2021, 1, 23)
    print(d)
    print(d.add_days(40))
    print(d.isoweekday())