from abc import ABC, abstractmethod

from .container import Container
from .curry import curry2

class Functor(ABC, Container):

  @abstractmethod
  def fmap(self, fn):
    pass

@curry2
def fmap(fn, f):
  return f.fmap(fn)
