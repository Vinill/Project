#!/usr/bin/python3

class Tienda:
    def __init__(self, name, price, size, company, brand, gender):
        self.name = name
        self.price = price
        self.size = size
        self.company = company
        self.brand = brand
        self.gender = gender

    def product(self, clothing, footwear, accessories):
        self.clothing = clothing
        self.footwear = footwear
        self.accessories = accessories
    
    @property
    def size(self)
        return(size.size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
            

    