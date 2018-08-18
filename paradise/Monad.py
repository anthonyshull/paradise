from abc import ABC, abstractmethod

from .Functor import Functor
from .Pointed import Pointed

class Monad(Functor, Pointed):
  
  def chain(self, fn):
    return self.fmap(fn).join()

  @abstractmethod
  def join(self):
    pass

def chain(fn, m):
  return m.chain(fn)

def join(m):
  return m.join()