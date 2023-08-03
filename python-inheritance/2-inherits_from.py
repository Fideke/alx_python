"""
a functiom
"""
def inherits_from(obj, a_class):
    """
    a function of obj and class
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class