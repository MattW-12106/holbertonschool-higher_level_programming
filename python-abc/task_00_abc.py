#!/usr/bin/env python3
"""
define an abstract class called Animal with an abstract method make_sound. 
Then, create two subclasses, Dog and Cat, that implement the make_sound method to return 
"Woof!" and "Meow!" respectively.
"""
import abc
"""This code defines an abstract class called Animal with an abstract method make_sound."""
class Animal(abc.ABC):
    """Abstract class representing an animal."""
    @abc.abstractmethod
    def make_sound(self):
        """Abstract method to be implemented by subclasses to return the sound made by the animal."""
        pass
class Dog(Animal):
    """Class representing a dog, inheriting from the Animal abstract class."""
    def make_sound(self):
        """Returns the sound made by a dog."""
        return "Woof!"
class Cat(Animal):
    """Class representing a cat, inheriting from the Animal abstract class."""
    def make_sound(self):
        return "Meow!"