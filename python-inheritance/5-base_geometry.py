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
        """
        a function area
        """
        raise Exception("area() is not implemented")

        """
        a function that defines name , value
        """
    def integer_validator(self, name, value):
        """
        a function
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")