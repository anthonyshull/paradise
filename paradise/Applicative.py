from .functor import Functor
from .pointed import Pointed


class Applicative(Functor, Pointed):

  def ap(self, a):
    return a.fmap(self.value)
