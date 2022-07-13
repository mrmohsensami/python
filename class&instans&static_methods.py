# method => 1.instance, 2.class, 3.static

import datetime

class Person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self):
        print(f'{self.name} is {self.height}')

    @classmethod
    def from_birth(cls, name, height, age):
        return cls(name, height, datetime.datetime.now().year - age)

    @staticmethod
    def is_adult(age):
        if age > 18:
            print('Yes')
        else:
            print('No')

p1 = Person.from_birth('bob', 180, 1990)

p1.show()

p1.is_adult(22)
