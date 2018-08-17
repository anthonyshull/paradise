class Functor:

  def __init__(self, value):
    self.value = value

  def _map(self, fn):
    return fn(self.value)

def map(fn, f):
  return f.map(fn)