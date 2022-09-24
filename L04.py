# scopes - variables & functions

from typing import ClassVar


i = 7

def my_f():
    i = 5
    return i

print(i)
# 7
i = my_f()
print(i)
# 5

# variables used as functions
f = my_f
print(f())
# 5

# empty class - pass or return?

class Animal:
    # return gives error
    pass # no error

# my_animal = Animal()



# class attributes & methods - adding self
class Animal:
    # hints!!!
    a: ClassVar[int] = 6
    b: ClassVar[int] = 8
    _a: ClassVar[int] = 16
    _b: ClassVar[int] = 18
    __a: ClassVar[int] = 26
    __b: ClassVar[int] = 28

    # getters and setters

    def get_a(self) -> int:
        return self.__a
        # errors without self

    def get_b(self) -> int:
        return self.b

    def set_a(self, param1: int) -> None:
        return self.__My_private_func(param1)
    
    def set_b(self, param1: int) -> None:
        self.b = param1

    def __My_private_func(param):
        return "7"

# ???
    

my_animal = Animal()
# print(my_animal.a)
# print(my_animal.return_a())

my_animal.set_a(12)
print(f"Animal 1 has an a value of {my_animal.get_a()}")

my_animal2: Animal = Animal()
print(f"Animal 2 has an a value of {my_animal2.get_a()}")


print(f"my animal a value is {my_animal.a}") # accessible by everyone
print(f"my animal _a value is {my_animal._a}") # should access using method
# print(f"my animal __a value is {my_animal.__a}") # fully private, need methods

print(f"my animal __a value is {my_animal.get_a()}") # fully private, need methods

# good habit to set up everything as private with __ and use getters & setters

"""
class classname:
    __variable = ...
    def get_variable(self):
        return self.variable
    def set_variable(self):
        ...
"""