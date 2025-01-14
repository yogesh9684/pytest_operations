import pytest
@pytest.mark.Login
def test_m1():
    a=20
    b=20
    assert a==b,'We are good'

def test_m2():
    c='yogesh'
    assert c.upper()=='YOGESH'


def test_m3():
    assert 'current' == 'current'

@pytest.mark.Login
def test_m4():
    assert 'admin'=='admin'

@pytest.mark.Login
def test_m5():
    assert 'YogaYog' == 'YogaYog'
