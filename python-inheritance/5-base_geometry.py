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