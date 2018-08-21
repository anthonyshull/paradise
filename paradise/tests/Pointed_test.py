from ..pointed import Pointed


class IO(Pointed):
  pass


def test_pointed_of():
  io = IO.of(True)
  assert io.value
