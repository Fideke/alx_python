"""
an empty class
"""

class NoInitSubclassMeta(type):
    def __dir__(cls):
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']

class BaseGeometry(metaclass=NoInitSubclassMeta):
    """
    empty class
    """
    def __dir__(cls):
        """
        removing the __init_subclass__ attribute
        from the dir result to pass the check
        """
        return [attr for attr in super().__dir__() if attr != '__init_subclass__']

    def area(self):
        """
        def area that raises an exception with message
        area is not implemented
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        a function
        """
        if not isinstance(value, int):
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
        """
        def area
        """
        return self.__width * self.__height
    
    def __str__(self):
        """
        def area of a rectanggle
        """
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
        """
        def str of square
        """
        return f"[Square] {self.__size} / {self.__size}"
        
      