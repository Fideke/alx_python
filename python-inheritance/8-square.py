"""
an empty class
"""
class BaseGeometry:
    """
    empy class
    """
    pass

    """
    a function that defines area and raise exception
    """
    def area(self):
        raise Exception("area() is not implemented")

        """
        a function that defines name , value
        """
    def integer_validator(self, name, value):
        if value is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        

"""
a class rectangle that inherits from BaseGeometry
"""
class Rectangle(BaseGeometry):
    """
    inherited class
    """
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    
    def area(self):
        return self.__width * self.__height
    
    def __str__(self):
        return f"[Rectangle] {self.__Width} / {self.__height}"
    

"""
a square class
"""
class Square(Rectangle):
    """
    a square class that inherits from rectangle
    """
    def __init__(self, size):
        self.__size = 0
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
    
   
    def __str__(self):
        return f"[Square] {self.__size} / {self.__size}"
        
      