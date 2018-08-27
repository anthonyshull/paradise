def curry2(fn):
  def fn1(x):
    def fn2(y):
      return fn(x, y)
    return fn2
  return fn1


def curry3(fn):
  def fn1(x):
    def fn2(y):
      def fn3(z):
        return fn(x, y, z)
      return fn3
    return fn2
  return fn1