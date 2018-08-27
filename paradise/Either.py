from .monad import Monad


class Left(Monad):

  def fmap(self, fn):
    return self

  def join(self):
    return self


class Right(Monad):

  def fmap(self, fn):
    return Right(fn(self.value))

  def join(self):
    return self.value


def is_left(m):
  return type(m) == Left


def is_right(m):
  return type(m) == Right
