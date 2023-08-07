"""
create a file named models with an empty fil __init__.py,
inside with this file, the folder will become python package
"""

class Base:
   """
   create a file named models/base.py
   class base
   class constructor: def __init__(self, id=None):
   """
   __nb_objects = 0

   def __init__(self, id=None):
      if id is not None:
         self.id = id
      else:
          Base.__nb_objects =+ 1
          self.id = Base
