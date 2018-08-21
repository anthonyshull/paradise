from abc import ABC, abstractclassmethod

from .semigroup import Semigroup


class Monoid(Semigroup, ABC):

  @property  # type: ignore
  @abstractclassmethod
  def identity(self):
    pass

  @identity.setter
  def identity(self, identity):
    pass
