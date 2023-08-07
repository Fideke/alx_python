#!/usr/bin/python3
"""
write the class Rectangle that inherits from Base
"""
import json
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
         
         """protect attribute of our class"""

         return self.__width
        
        @property
        def height(self):

            """protect attribute of our class"""

            return self.__height
        
        @property
        def x(self):
         
         """protect attribute of our class"""

         return self.__x
        
        @property
        def y(self):
         
         """protect attribute of our class"""

         return self.__y
        
        
        @width.setter
        def width(self, value):    
             """validate what adeveloper is trying to assign a variable"""

             if type(value) is not int:
                raise TypeError("width must be an integer")
             if value <= 0:
                raise ValueError("width must be > 0")
             self.__width = value
             
            
        @height.setter
        def height(self, value):
            """validate what adeveloper is trying to assign a variable"""

            if type(value) is not int:
               raise TypeError("height must be an integer")
            if value <= 0:
               raise ValueError("height must be > 0")
            self.__height = value
    

        @x.setter
        def x(self, value):
            """validate what adeveloper is trying to assign a variable"""

            if type(value) is not int:
               raise TypeError("x must be an integer")
            if value < 0:
               raise ValueError("x must be >= 0")
            self.__x = value
           

        @y.setter
        def y(self, value):
            """validate what adeveloper is trying to assign a variable"""

            if type(value) is not int:
               raise TypeError("y must be an integer")
            if value < 0:
               raise ValueError("y must be >= 0")
            self.__y = value
            



        
