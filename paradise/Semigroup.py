from abc import ABC, abstractmethod

from .Container import Container

class Semigroup(Container, ABC):
  
  @abstractmethod
  def add(self, other):
    pass

  def __add__(self, other):
    return self.add(other)

  def __radd__(self, other):
    return other.add(self)