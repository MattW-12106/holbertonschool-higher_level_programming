#!/usr/bin/env python3
""" 
defines a class VerboseList that inherits from list and overrides some of its methods 
to print messages when they are called.
"""
class VerboseList(list):
    def append(self, item):
        print(f"Added {item} to the list")
        super().append(item)
    def extend(self, iterable):
        print(f"Extending the list with {iterable}")
        super().extend(iterable)
    def remove(self, item):
        print(f"Removing {item} from the list")
        super().remove(item)
    def pop(self, index=-1):
        print(f"Popping item at index {index}")
        return super().pop(index)