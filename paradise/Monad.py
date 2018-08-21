from abc import ABC, abstractmethod

from .applicative import Applicative


class Monad(Applicative):

  def chain(self, fn):
    return self.fmap(fn).join()

  @abstractmethod
  def join(self):
    pass


def chain(fn, m):
  return m.chain(fn)


def join(m):
  return m.join()
