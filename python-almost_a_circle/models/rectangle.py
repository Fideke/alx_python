

"""
write the class Rectangle that inherits from Base
"""
from models.base import Base

class Rectangle(Base):
    """
    private instance attributes , each with its own public getter and setter
    __width
    __height
    __x
    __y
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class constructor, call the super class with id, this super call with
        use the logic of the __init__ of the Base class
        Assign each arguement width, height, x, y to the right attribute
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @property
        def width(self):
            """
             protect attributes of our class
            """
            return self.__width
        
        @width.setter
        def width(self, value):
             """
             with the setter you are able to validate what adeveloper is trying 
            to assign to a variable
            """
             self.__width = value
             
            

        @property
        def height(self):
            return self.__height
        
        @height.setter
        def height(self, value):
            self.__height = value
            """
             with the setter you are able to validate what adeveloper is trying 
            to assign to a variable
            """

        @property
        def x(self):
         """
             protect attributes of our class
         """
        return self.__x
        
        @x.setter
        def x(self, value):
            self.__x = value
            """
             with the setter you are able to validate what adeveloper is trying 
            to assign to a variable
            """

        @property
        def y(self):
            """
             protect attributes of our class
            """
            return self.__y
        

        @y.setter
        def y(self, value):
            self.__y = value
            """
             with the setter you are able to validate what adeveloper is trying 
            to assign to a variable
            """



        