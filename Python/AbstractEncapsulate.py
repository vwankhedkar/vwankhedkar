from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        print("Barking")

animal = Dog()
animal.make_sound()
OUTPUT
Barking
**************************************************
from abc import ABC, abstractmethod
class Computer(ABC):
    @abstractmethod
    def process(self):
        pass
class Laptop(Computer):
    def process(self):
        print("It's running")
class programmr:
    def work(self, com):
        print("Solving bugs")
        com.process()

com1 = Laptop()
com1.process()
prog1 = programmr()
prog1.work(com1)
OUTPUT
It's running
Solving bugs
It's running
****************************************************
class Car:
    def __init__(self):
        self.__speed = 0  # Private attribute

    def accelerate(self, value):
        self.__speed += value

    def get_speed(self):  # Getter method
        return self.__speed

car = Car()
print(car.get_speed())  # Correct way to access private attribute
OUTPUT - 0

