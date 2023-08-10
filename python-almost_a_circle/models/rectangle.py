#!/usr/bin/python3
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
            
    def area(self):
        """
        a public method that returns the value of the rectangle instancle
        """
        return self.__width * self.__height
    
    def display(self):
        """
        a public method that prints in stdout the rectangle instance 
        with the character # 
        no need to handle X and y
        """
        for y in range(0, self.__x):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end=" ")
            print()

    def __str__(self):
        """
        overridding the __str__ method so that it returns [rectangle]
        """
        s = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height)
        return s
    
    def update(self, *args, **kwargs):
        """
        public method that assigns an arguement to each attribute
        1st args id attribute
        2nd args width attribute
        3rd args height attribute
        4th args x attribute
        5th args y attribute
        """
        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    if type(value) != int and value is not None:
                        raise TypeError("id must be an integer")
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key =="x":
                    self.x = value
                if key == "y":
                    self.y = value
                    









            
