# # asd = [1,2,3,4,5,6,7,8]

# # inp = int(input('Введите индекс элемента списка: '))
# # inp2 = input('Введите новое значение: ')

# # asd[inp] = inp2
# # print(asd)
# # for i,v in enumerate(asd):
# #     if inp == i:
# #         asd[i] = inp2
# # print(asd)

# from abc import ABC, abstractmethod

# class AbstractClass(ABC):
    
#     def __init__(self,name, last_name):
#         self.name = name
#         self.last_name = last_name

#     @abstractmethod # --> он должен быть переопределен    
#     def abst_func(self):
#         pass


# class A(AbstractClass):
#     def __init__(self, name, last_name, additional):
#         super().__init__(name, last_name)
#         self.additional = additional

#     def abst_func(self):
#         self.abst_func()


# a = A('asd', 'qwe')
# a.my_func()

# # на примере абстракции: Тим лид задает абстракный класс и абстрактные методы а также условие задачки а обычные разработчики импортируют встреонный модуль from abc import ABC, abstractmethod и его методы нужны переопределить и выполнить задание

from datetime import datetime
class SmartPhones:
    def __init__(self, name, color, memory, battery=0):
        self.name = name
        self.color = color
        self.name = name
        self.name = name
        self.memory = memory
        self.battery = battery
    def str(self):
        return self.name

    def charge(self, value):
        self.battery += value
class Iphone(SmartPhones):
    def __init__(self,ios, name, color, memory, battery=0):
        super().__init__(name, color, memory=0, battery=0)
        self.ios = ios
    def send_imessage(self, str_):
        self.str_ = str_
        return f'sending {self.str_} from {self.name}'
class Samsung(SmartPhones):
    def __init__(self, android, name, color,memory, battery=0):
        super().__init__(name, color, memory, battery=0)
        self.android = android
    def show_time(self):
        time = datetime.now()
        return time

        
phone = SmartPhones('Xiaomi', 'red', '128GB')
iphone7 = Iphone('IOS7', 'Iphone 7', 'orange', '256GB')
samsung = Samsung('Android 9', 'Samsung galaxy A7 2016', 'Black', '64BG')
print(phone.str(), phone.charge(60))
print(iphone7.str(), iphone7.charge(100), iphone7.send_imessage('Asd'))
print(samsung.str(), samsung.charge(70), samsung.show_time())


