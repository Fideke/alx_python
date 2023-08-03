"""
square that definews a square by based on 0-square.py
"""
class Square:
    
  """
   defining the class
  """

  def __init__(self, size=0):
        self.__size = size
        while type(size) is int:
          if size < 0:
             raise ValueError("size must be >= 0")
        else:
           raise TypeError("size must be an integer")
