from ..Monoid import Monoid
from ..Semigroup import Semigroup

class Integer(Semigroup):

  def combine(self, other):
    return Integer(self.value + other.value)

class IntegerUnderAddition(Integer, Monoid):

  identity = Integer(0)

def test_monoid_identity():
  integer_under_addition = IntegerUnderAddition(1)
  assert (integer_under_addition + integer_under_addition.identity).value == integer_under_addition.value