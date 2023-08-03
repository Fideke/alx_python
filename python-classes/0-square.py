"""
a square class

"""

class Square:
    """
    class square that defines a square by private instance attribute: size
     size of a square is crucial for a square, many things depend on it area, perimeter 
    """
    def __init__(self, size):
        self.__size = size
