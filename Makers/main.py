# функция полиморфизма - len()
# print(len('Makers'))
# print(len([1,2,3,4,5]))
# print(len({1:2, 2:3, 3:4}))

# (__add__) - метод полиморфизма:
# print(5+5)
# print('Asd' + 'Luxury')
# print([1,2,3] + [4,5,6])
# print({1:2, 3:4, 5:6})

# полиморфизм - способность функции (метода) обрабатывать данные разных типов данных (int,str,tuple, list, set...)

# list.pop()
# set.pop()
# dict.pop()

    # Широко распространённое определение полиморфизма: Один интерфейс - много реализаций

# class Cat:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def info(self):
#         print(f'Its a cat. Cats name is {self.name}, age {self.age}')

#     def make_sound(self):
#         print('Meow, meow!')

# class Dog:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age

#     def info(self):
#         print(f'Its a dog. Dogs name is {self.name}, age {self.age}')

#     def make_sound(self):
#         print('Bark, bark!')

# animal = Cat('Kisa', 1.5)
# animal.info()
# animal.make_sound()

# animal2 = Dog('Aktosh', 2.5)
# animal2.info()
# animal2.make_sound()


# from math import pi

# class Shape:
#     def __init__(self, name):
#         self.name = name 

#     def area(self):
#         pass
#     def fact(self):
#         return 'Я фигура в двумерной плоскости'
    
#     def __str__(self):
#         return self.name

# class Square(Shape):
#     def __init__(self, length):
#         super().__init__('Square')
#         self.length = length

#     def area(self):
#         return self.length ** 2

#     def fact(self):
#         return 'У квадрата все углы равны  90 градусам!'

# class Circle(Shape):
#     def __init__(self, radius):
#         super().__init__('Circle')
#         self.radius = radius

#     def area(self):
#         return pi * self.radius ** 2
    
#     # def fact(self):
#     #     return 'У круга 360 градусов!'

# a = Square(4)
# b = Circle(7)
# print(a)
# print(b)
# print(a.area())
# print(b.area())
# print(a.fact())
# print(b.fact())

# c = Shape('Asd')
# print(c.area())
# print(c.fact())

# class Duck:
#     def quack(self):
#         print('Quaaaaak!')
#     def feathers(self):
#         print('The duck has white and gray feathers!')
    
# class Person:
#     def quack(self):
#         print('Person imitates a duck')

#     def feathers(self):
#         print('Person takes a feathers from the ground!')

# def in_the_forest(obj):
#     obj.quack()
#     obj.feathers()

# asd = Person()
# qwe = Duck()

# in_the_forest(asd)
# in_the_forest(qwe)


# class Telephone:
#     power = 100
#     def __init__(self, name, model, imei , oc):
#         self.name = name
#         self.model = model
#         self.imei = imei
#         self.oc = oc
#     @property
#     def get_info(self):
#         print(f'Смартфон: {self.name} \n Модель: {self.model}\n Имей код: {self.imei} \n Операционная система: {self.oc}\n Эмкость батареи: {self.power}%')
#     @property  
#     def music(self):
#         print('Music')
#         self.power = self.power - 5
#         if self.power <= 0:
#             print('Заряд батареи заряжен!')
#     @property
#     def video(self):
#         print('video')
#         self.power = self.power - 7
#         if self.power <= 0:
#             print('Заряд батареи заряжен!')


# xiaomi = Telephone('Xiaomi RedMi', 'Node 9s', 2425122000, 'Android')
# i = 0
# while  i <= 15:
#     xiaomi.video
#     i+=1

# xiaomi.get_info


# @property - делает функцию без скобок что бы мы могли обращаться к функциям как к атрибуту


        