from ..Semigroup import Semigroup

class Integer(Semigroup):

  def combine(self, other):
    return Integer(self.value + other.value)

def test_semigroup_create():
  assert Integer(1).value == 1
  
def test_semigroup_add():
  assert (Integer(1) + Integer(2)).value == Integer(3).value

def test_semigroup_radd():
  assert (Integer(2) + Integer(1)).value == Integer(3).value