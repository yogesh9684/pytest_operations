import pytest

@pytest.mark.sanity
def test_sample_one():
    print("Printing sample Testing One")

@pytest.mark.smoke
def test_sample_two():
    print("Printing sample Testing Two")

@pytest.mark.sanity
def test_sample_three():
    print("Printing sample Testing Three")