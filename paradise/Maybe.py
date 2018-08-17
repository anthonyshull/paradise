from Functor import Functor
from Monad import Monad

class Maybe(Monad, Functor):

  def is_nothing(self):
    if self.value is None:
      return True
    else:
      return False

  def map(self, fn):
    if self.is_nothing:
      return Nothing()
    else:
      return Just(self._map(fn))
  
  def __not__(self):
    return self.is_nothing()

class Just(Maybe):
  pass

class Nothing(Maybe):

  def __init__(self):
    self.value = None