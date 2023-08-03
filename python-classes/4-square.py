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
    
    """
    getter and setter methods
    validating private attribute
    """
    @property
    def size(self):
         return self.__size
    
    @size.setter
    def size(self, value):
         self.__size = value
         while type(value) is int:
               if value < 0:
                        raise ValueError("size must be >= 0")
               break
         else:           
                raise TypeError("size must be an integer")
         
         """
         public instance method
         """
    def my_print(self):
         if self.__size == 0:
               print("")
         else:
              for i in range(0, self.__size):
                            for j in range(0, self.__size):
                                  print("#", end="")
                            print("")
        