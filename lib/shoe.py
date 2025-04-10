#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size # Assuming initial validation is not required here

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")
            self._size = None  # You can choose to raise an exception instead of setting it to None

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")
