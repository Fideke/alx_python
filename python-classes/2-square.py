"""
a class that defines a square
"""
class Square:
    """
    defining square object
   
    size is assumed to be an int
    """
    def __init__(self, size=0):
            self.__size = size 
            """private attribute"""
            while type(size) is int:
                  if size < 0:
                        raise ValueError("size must be >= 0")
                  break
            else:           
                raise TypeError("size must be an integer")
    """
    public instance method 
    
    """
    def area(self):
     return self.__size ** 2