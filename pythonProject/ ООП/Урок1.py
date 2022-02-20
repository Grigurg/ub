import pprint


class Person:
    name = 'Ivan'
    age = 30


pprint.pprint(Person.__dict__)
print(getattr(Person, 'name'))
print(getattr(Person, 'x', 100))
Person.name = 'Vasy'
print(Person.name)
Person.x = 100
print(Person.x)
setattr(Person, 'y', 300)
del Person.x
delattr(Person, 'y')
print(Person.__dict__)
a = [1, 2, 3]
b = a.copy()
print('Да пашёл ты нахуй' if id(a) == id(b) else 'Ура')
