from ..either import Left, Right


def test_left_fmap():
  left = Left(True).fmap(lambda x: not x)
  assert isinstance(left, Left)
  assert left.value


def test_left_join():
  left = Left.of(Left.of(True)).join()
  assert isinstance(left, Left)
  assert isinstance(left.value, Left)


def test_left_chain():
  left = Left(True).chain(lambda x: Right(not x))
  assert isinstance(left, Left)
  assert left.value


def test_right_fmap():
  right = Right(True).fmap(lambda x: not x)
  assert isinstance(right, Right)
  assert not right.value


def test_right_join():
  right = Right.of(Right.of(True)).join()
  assert isinstance(right, Right)
  assert right.value


def test_right_chain():
  right = Right(True).chain(lambda x: Right(not x))
  assert isinstance(right, Right)
  assert not right.value
