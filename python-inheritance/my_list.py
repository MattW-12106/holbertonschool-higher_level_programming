#!/usr/bin/python3
"""class mylist that inherits from list"""
class MyList(list):
    """ 
        class MyList that inherits from list.

        >>> my_list = MyList([3, 1, 2])
        >>> my_list.print_sorted()
        [1, 2, 3]
        >>> my_list.append(0)
        >>> my_list.print_sorted()
        [0, 1, 2, 3]
        >>> my_list
        [3, 1, 2, 0]
    """
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))