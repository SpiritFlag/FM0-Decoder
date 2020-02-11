import numpy as np

class IQcomplex:
  def __init__(self):
    self.real = 0
    self.imag = 0

  def __init__(self, _real, _imag):
    self.real = _real
    self.imag = _imag

  def print(self):
    print("<" + str(self.real) + ", " + str(self.imag) + ">")

  def add(self, complex):
    return IQcomplex(self.real+complex.real, self.imag+complex.imag)

  def mul(self, complex):
    return IQcomplex(self.real*complex.real, self.imag*complex.imag)

  def div(self, complex):
    return IQcomplex(self.real/complex.real, self.imag/complex.imag)

  def s_add(self, scalar):
    return IQcomplex(self.real+scalar, self.imag+scalar)

  def s_rev_sub(self, scalar):
    return IQcomplex(scalar-self.real, scalar-self.imag)

  def distance(self, complex):
    return np.sqrt((self.real - complex.real) ** 2 + (self.imag - complex.imag) ** 2)
