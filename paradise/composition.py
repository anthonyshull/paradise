# BATTERIES INCLUDED
from functools import reduce

def pipe(fns):
  def run(arg):
    return reduce(lambda app, fn: fn(app), fns, arg)
  return run