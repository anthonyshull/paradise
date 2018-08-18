from ..Functor import Functor, fmap

class List(Functor):

  def fmap(self, fn):
    return List(list(map(fn, self.value)))

def double(x):
  return x * 2

xs = List([1, 2, 3])

def test_functor_fmap():
  double_xs = xs.fmap(double)
  assert double_xs.value == List([2, 4, 6]).value

def test_fmap():
  double_xs = fmap(double, xs)
  assert double_xs.value == List([2, 4, 6]).value

def test_fmap_functor_fmap():
  assert fmap(double, xs).value == xs.fmap(double).value