"""
class square that inherits fro rectangle
"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """
    class square inherits from rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        call tthe super class with id, x, y, width, and height this super call will
        use logic of init of the rectangle class
        """
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        method should return
        """
        s = "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.__width)
        return s
    

    @property
    def size(self):
        """
        retrives the size
        """
        return self.__width
    
    @size.setter
    def size(self, value):
        """
        sets the size
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width =  value
        self.__height = value

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