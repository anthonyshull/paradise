from .container import Container


class Pointed(Container):

  @classmethod
  def of(self, value):
    return self(value)
