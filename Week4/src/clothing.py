class Clothing:

    def __init__(self, color, material, size):
        self.__color = color
        self.__material = material
        self.__size = size

    def __repr__(self):
        return f'clothing (color={self.__color}, material={self.__material}), size={self.__size}'

    def __str__(self):
        return f'color is {self.__color}, {self.__material} material, {self.__size} size'
    