from ..Monoid import Monoid

class Integer(Monoid):

  def add(self, other):
    return Integer(self.value + other.value)

  @property
  def identity(self):
    return self._identity

  @identity.setter
  def identity(self, identity):
    self._identity = identity

def test_monoid_identity():
  integer = Integer(1)
  integer.identity = Integer(0)
  assert (integer + integer.identity).value == integer.value