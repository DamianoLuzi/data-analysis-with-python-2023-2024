'''Module for right triangle computations'''
__author__ = 'Damiano Luzi'
__version__ = '1.0'
import math
def hypotenuse(x,y):
  '''Returns the hypoteuse of a right triangle given lengths of two other sides'''
  return math.sqrt(x**2+y**2)
def area(x,y):
  '''Returns the area of the right triangle when sides are given as parameters.'''
  return float(x*y/2)