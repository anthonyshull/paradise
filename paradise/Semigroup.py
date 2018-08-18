from abc import ABC, abstractmethod

from .Container import Container

class Semigroup(Container, ABC):
  
  @abstractmethod
  def combine(self, other):
    pass

  def __add__(self, other):
    return self.combine(other)

  def __radd__(self, other):
    return other.combine(self)