# BATTERIES INCLUDED
from typing import Iterator, List, TypeVar

T = TypeVar('T')

def head(l: List[T]) -> T:
  return l[0]

def tail(l: List[T]) -> List[T]:
  return l[1:]

def flatten(l: Iterator[Iterator[T]]) -> List[T]:
  return [j for i in l for j in i]