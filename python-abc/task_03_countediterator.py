#!/usr/bin/env python3
"""
defines a class CountedIterator that takes an iterable and allows you to iterate over it 
while keeping track of how many items have been iterated over.
"""
class CountedIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < len(self.iterable):
            item = self.iterable[self.count]
            self.count += 1
            return item
        else:
            raise StopIteration