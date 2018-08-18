from .Monad import Monad

class Maybe(Monad):
  
  def fmap(self, fn):
    if self.is_nothing():
      return Nothing(None)
    else:
      return Just(self.fmap(fn))

  def join(self):
    if self.is_nothing():
      return Nothing(None)
    else:
      return self.value
  
  def is_nothing(self):
    if self.value is None:
      return True
    else:
      return False

  def is_just(self):
    if self.value is not None:
      return True
    else:
      return False
  
  def __not__(self):
    return self.is_nothing()

class Just(Maybe):
  pass

class Nothing(Maybe):
  pass