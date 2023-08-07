"""
create a folder named models with an empty file __init__.py inside with this file,
the folder will become a python package
create a file named models/base.py
"""
class Base:
    """
    private class attribute __nb_objects = 0, class constructor: def __init__(self, id=None)
    
    """
    __nb_objects = 0


    def __init__(self, id=None):
        """
        if id is not none , assign the public instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        