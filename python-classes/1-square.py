"""
square that definews a square by based on 0-square.py
"""
class Square:
    
  """
   defining the class
  """

  def __init__(self, size=0):
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
