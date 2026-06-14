import pytest

from api_test4 import bmi_kalkulator


@pytest.fixture
def przykladowy_pacjent():
    return {"waga": 80, "wzrost": 1.67}

def test_bmi_normalny(przykladowy_pacjent):
    assert round(bmi_kalkulator(przykladowy_pacjent["waga"], przykladowy_pacjent["wzrost"]), 2) == 28.69