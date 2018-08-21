from abc import ABC, abstractmethod

from .container import Container


class Functor(ABC, Container):

  @abstractmethod
  def fmap(self, fn):
    pass


def fmap(fn, f):
  return f.fmap(fn)
