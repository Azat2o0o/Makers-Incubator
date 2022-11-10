# class Stream:
#     def __str__(self) -> str:
#         return 'John\'s stream!'

# class Logger:
#     def __init__(self) -> None:
#         self.stream = None

#     def print_the_stream(self):
#         if self.stream:
#             print(f'Stream from class: {self.stream}')
#         else:
#             print('None stream!')

# logger = Logger()
# logger.stream = Stream()
# # # logger.stream = Stream2()
# logger.print_the_stream()


# class Engine:
#     country = 'Germany'
#     def __init__(self, power):
#         self.power = power

#     def __str__(self):
#         return f'Country: {self.country} -> Engine: {self.power}'

# class Car:
#     model = 'Audi'
#     country = 'Germany'
#     def __init__(self, type, power):
#         self.engine = Engine(power)
#         self.type = type
#     def __str__(self):
#         return f'{self.model} {self.type} -> Engine: {self.engine} -> Country: {self.country}'


# car = Car('A8', 360)
# print(car)

import json

FILE = 'users_info.py'
class Users:
    def validate(self, password, password2):
        self.password = password
        self.password2 = password
        if len(password) < 8:
            raise ValueError('Пароль должен состоять из 8 символов или больше!')
        elif password.isdigit() or password.isalpha():
            raise ValueError('Пароль должен состоять из букв и цифр!')
        elif password2 != password:
            raise ValueError('Пароли не совпадают!')
        
    def sign_up(self,username, password, password2):
        self.validate(password, password2)
        self.username = username
        with open(FILE, 'r') as file:
            try:
                data = json.load(file)
                id = data[-1['id'] + 1
            except:
                data = []
                id = 1
        with open(FILE, 'w') as file:
            if data:
                is_username_used = any([x['name'] == name for x in data])
                if is_username_used:
                    data.json           
                    raise 

# ____________________________________________________________________________________________________________________

# class methods, instance methods, static methods

# Методы экземпляра класса(Instance methods), - это те методы в ООП которые изменяют состояние экземпляра класса:
# def methods(self) - self ссылка на экземпляра

# методы класса (class Methods) - это те методы  которые могут изменять состояние самого класса и манипулировать самим классом:
# @classmethods - декоратор который определяет метод класса
# def method(cls) - cls это ссылка на сам класс 

# Статические методы (Static methods) - это те методы которые не могут изменять состояние ни экземпляра от класса ни самого класса
# @staticmethod декоратор который определяет статик метод  
# def nethod():


# class Student:
#     school_name = 'ABC school'

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(self.name, self.age, 'School:', Student.school_name)

#     @classmethod
#     def change_school(cls, name):
#         # print('!!!',cls)
#         # class_name.class_variable
#         cls.school_name = name

# john = Student('John', 20)
# john.show()
# john.change_school('Nazarbaev school')
# john.show()

# class Person:
#     surname = 'Mercedes'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     @staticmethod
#     def is_adult(age):
#         if age >=18:
#             print('Person is adult!')
#         else:
#             print('Not adult!')
#     @classmethod
#     def from_birth_date(cls, name, year):
#         from datetime import date
#         cls.surname = 'Ergeshova'
#         age = date.today().year - year
#         return cls(name, age)
        
# # asd = Person('Azat', 22)
# # print(asd.name, asd.surname, asd.age)
# # Person.is_adult(asd.age)
# # asd.is_adult(14)

# ram = Person.from_birth_date('Ramina', 2003)
# print(ram.name, ram.surname, ram.age)

# class Person:
#     name = 'John'
#     @classmethod
#     def change_name(cls, name):
#         cls.name = name

# asd = Person()
# print(asd.name)
# asd.change_name('Asd')
# print(asd.name)