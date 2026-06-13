import pytest

def bmi_kalkulator (waga, wzrost):
    return waga / (wzrost * wzrost)

def test_bmi_kalkulator ():
    assert round(bmi_kalkulator(70, 1.75), 2) == 22.86

@pytest.mark.parametrize("waga, wzrost, oczekiwane", [
    (70, 1.75, 22.86),
    (50, 1.60, 19.53),
    (90, 1.80, 27.78)
])

def test_bmi_parametrize(waga, wzrost, oczekiwane):
    assert round(bmi_kalkulator(waga, wzrost), 2) == oczekiwane

def test_zero():
    with pytest.raises(ZeroDivisionError):
        bmi_kalkulator(70,0)