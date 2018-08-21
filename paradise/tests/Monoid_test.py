from ..monoid import Monoid
from ..semigroup import Semigroup


class Integer(Semigroup):

  def combine(self, other):
    return Integer(self.value + other.value)


class IntegerUnderAddition(Integer, Monoid):

  identity = Integer(0)  # type: ignore


def test_monoid_identity():
  i_u_a = IntegerUnderAddition(1)
  assert (i_u_a + i_u_a.identity).value == i_u_a.value
