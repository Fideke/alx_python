"""
a function 
"""
def is_kind_of_class(obj, a_class):
    """
    a function that returns true if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class; otherwise false
    """
    return isinstance(obj, a_class)