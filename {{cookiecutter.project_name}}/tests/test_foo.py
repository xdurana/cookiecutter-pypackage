import pytest

from {{cookiecutter.project_slug}}.foo import foo


@pytest.fixture
def bar() -> str:
    return "bar"


def test_foo(bar: str) -> None:
    assert foo(bar) == "foobar"
