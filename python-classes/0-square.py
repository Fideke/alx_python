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

    def area(self):
        return self.__size ** 2
    
    def perimeter(self):
        return 4 * self.__size
    
    def get_size(self):
        return self.__size
    
    def set_size(self, size):
        self.area__size = size
    
my_square = Square(3)
print(type(my_square))
print(my_square.__dict__)



        
  