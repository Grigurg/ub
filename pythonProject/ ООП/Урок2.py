# class Car:
#     model = 'BMW'
#     engine = 1.6
#
#
# a1 = Car()
# a2 = Car()
# print(a1.__dict__)
# a1.model = 'lada'
# print(a1.model)
# print(a2.model)


# class Car:
#     model = 'BMW'
#     engine = 1.6
#     def drive(self):
#         print('let s go')
#
#
# print(Car.__dict__)
# Car.drive('self')
# # a = Car.drive
# # a()
# # getattr(Car, 'drive')()
# # a = Car


# class Person:
#     def print_info(self):
#         print(f'Name: {self.name}\n'
#               f'Surmame: {self.sur_name}')
#
#
# p1 = Person
# p1.name = 'Иван'
# p1.sur_name = 'Иванов'
# p1.age = '12'
# p2 = Person
# p2.name = 'Пётр'
# p2.sur_name = 'Петров'
# p2.age = '23'
# p1.print_info(p1)
# class Point:
#     x = 1
#     y = 1
#
#     def setCoords(self, x, y):
#         self.x = x
#         self.y = y
#
#
# pt = Point()
# pt.setCoords(5, 10)
# print(pt.__dict__)
#
# class Point:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#         print('Создание экземпляра класса Point')
#     def __del__(self):
#         print('dek')
#
#     x = 1
#     y = 1
#
#
# pt = Point(5, 10)
# print(pt.__dict__)
# # Point.x = 2
# print(pt.x)
# class Point3D:
#
#     def __init__(self, x=0, y=0):
#         self.Cords = x, y
#
#     def set_cords(self, x, y):
#         self.Cords = x, y
#
#     def get_cords(self):
#         print(f'x = {self.Cords[0]}\n'
#               f'y = {self.Cords[1]}')
#
#     Cords = [3, 5]
#
#
# p1 = Point3D(8, 2)
# p1.get_cords()
# p1.set_cords(p1.Cords[0], 5)
# p1.get_cords()
# class Point:
#     mai = [2, 3, 4, 5]
#
#     def __init__(self, *args):
#         if args is None:
#             args = ['0' for i in range(len(mai))]
#         self.ass = args
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#
# lst = list()
# for i in range(2):
#     obj = Point(int(input('Введите x:')), int(input('Введите y:')))
#     lst.append(obj)
#
#
# print(lst[0].x)
# class Cat:
#     def __init__(self):
#         print('абракадабра', Cat.__dict__)
#
#
# tom = Cat()
# class Cat:
#     __shared_attr = {
#         'breed': 'pers',
#         'color': 'black'
#     }
#
#     def __init__(self):
#         self.__dict__ = Cat.__shared_attr
#
#
# a = Cat()
# b = Cat()
# a.breed = 'siam'
# print(a.__dict__)
# print(b.__dict__)
# class BankAccount:
#     def __init__(self, name, balance, passport):
#         self.__name = name
#         self.__balance = balance
#         self.__passport = passport
#
#     # def print_public_info(self):
#     #     print(f'{self.name}\n'
#     #           f'{self.balance}\n'
#     #           f'{self.passport}\n')
#
#     # def print_protected_info(self):
#     #     print(f'{self._name}\n'
#     #           f'{self._balance}\n'
#     #           f'{self._passport}')
#
#     def print_private_info(self):
#         print(f'{self.__name}\n'
#               f'{self.__balance}\n'
#               f'{self.__passport}')
#
#
# acc1 = BankAccount('Bob', 100000, 5467532874)
# acc1.print_protected_info()
# print(acc1.__name)
