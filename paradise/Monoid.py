from abc import ABC, abstractclassmethod

from .Semigroup import Semigroup

class Monoid(Semigroup, ABC):
  
  @property
  @abstractclassmethod
  def identity(self):
    pass

  @identity.setter
  def identity(self, identity):
    pass