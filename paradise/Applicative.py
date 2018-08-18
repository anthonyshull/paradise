from .Pointed import Pointed

class Applicative(Pointed):

  def ap(self, a):
    return a.map(self.value)