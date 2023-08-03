"""
class square
"""
class Square:
    """
    size must be an integer
    define an area of a square
    """
    def __init__(self, size=0):
        self.__size = size
        while size(type) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            break
        else:
            raise TypeError("size must be an integer")
        
    def area(self):
        return self.__size ** 2
