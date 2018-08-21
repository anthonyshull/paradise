from ..monad import Monad, chain, join


class Onion(Monad):

  def fmap(self, fn):
    return Onion(fn(self.value))

  def join(self):
    return self.value


def layer_onion(value):
  return Onion.of(value)


def test_monad_join():
  onion = Onion.of(True).fmap(layer_onion)
  assert onion.join().value


def test_monad_chain():
  onion = Onion.of(True).chain(layer_onion)
  assert onion.value


def test_join():
  onion = Onion.of(Onion.of(True))
  assert join(onion).value


def test_chain():
  onion = Onion.of(True)
  assert chain(layer_onion, onion).value
