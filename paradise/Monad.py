from abc import ABC, abstractmethod

from .applicative import Applicative
from .curry import curry2

class Monad(Applicative):

  def chain(self, fn):
    return self.fmap(fn).join()

  @abstractmethod
  def join(self):
    pass

@curry2
def chain(fn, m):
  return m.chain(fn)


def join(m):
  return m.join()
