from abc import ABC, abstractmethod

from .Container import Container

class Functor(ABC, Container):

  @abstractmethod
  def fmap(self, fn):
    pass

def fmap(fn, f):
  return f.fmap(fn)