from app import greet, greet_many


def test_greet():
    assert greet("Ada") == "Hello, Ada!"


def test_greet_many():
    assert greet_many("Ada", 1) == ["Hello, Ada!"]
    assert greet_many("Ada", 3) == ["Hello, Ada!"] * 3
