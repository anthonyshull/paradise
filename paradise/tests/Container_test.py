from ..container import Container


def test_container_create():
  container = Container(True)
  assert container.value
