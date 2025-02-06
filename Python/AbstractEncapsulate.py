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

