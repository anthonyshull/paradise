from invoke import task


@task
def test(c):
  c.run("pytest --pyargs paradise")


@task
def lint(c):
  c.run("pycodestyle --config=./.pycodestyle paradise")


@task(test, lint)
def build(c):
  return True
