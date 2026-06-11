import pytest
from kalkulator import dodaj, odejmij, mnoz, dziel

def test_dodaj():
    assert dodaj(2,3) == 5

def test_odejmij():
    assert odejmij(2,3) == -1

def test_mnoz():
    assert mnoz(2,3) == 6

def test_dziel():
    assert dziel(9,3) == 3

def test_dziel_edge():
    with pytest.raises(ZeroDivisionError):
        assert dziel(9, 0)