from abc import ABC, abstractmethod

from .Semigroup import Semigroup

class Monoid(Semigroup, ABC):
  
  @property
  @abstractmethod
  def identity(self):
    pass

  @identity.setter
  def identity(self, identity):
    pass