from Container import Container

class Monad(Container):

  def __init__(self, value):
    self.value = value
  
  def _bind(self, fn):
    pass

def bind(fn, m):
  return m.bind(fn)