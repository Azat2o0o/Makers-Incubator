# Создайте абстрактный класс DaysAndDates с двумя методами: define_date и define_days. Создайте три дополнительных класса: Current, MonthStart и MonthEnd. В Current необходимо вывести текущую дату. В MonthStart вывести первый день текущего месяца и кол-во дней с первого дня до текущего дня. В MonthEnd вывести последний день текущего месяца и кол-во дней до конца месяца.
# Даты выводить в формате: день/месяц/год, кол-во дней: в int.
# К абстрактным методам добавить док-стринг с описанием методов.

from abc import ABC, abstractclassmethod, abstractmethod
from datetime import datetime
class DaysAndDates:
    @abstractmethod
    def define_date(self):
        pass

    def define_days(self):
        pass
class Current:
    def define_date(self):
        date = datetime.today().strftime('%D')
        return  date
class MonthStart:
    
class MonthEnd:
    pass

asd = DaysAndDates()
print(asd.define_date())