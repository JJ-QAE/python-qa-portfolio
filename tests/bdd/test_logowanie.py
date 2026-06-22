import pytest
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../../features/logowanie.feature")

UŻYTKOWNICY = {
    "admin@test.com": "Admin123"
}

@given(parsers.parse('użytkownik podaje login "{login}" i hasło "{hasło}"'))
def podaj_dane(dane_logowania, login, hasło):
    dane_logowania["login"] = login
    dane_logowania["hasło"] = hasło

@when("system sprawdza dane")
def sprawdz_dane():
    pass

@then("użytkownik zostaje zalogowany")
def zalogowany(dane_logowania):
    login = dane_logowania["login"]
    hasło = dane_logowania["hasło"]
    assert UŻYTKOWNICY.get(login) == hasło

@then(parsers.parse('użytkownik widzi błąd "{komunikat}"'))
def błąd_logowania(dane_logowania, komunikat):
    login = dane_logowania["login"]
    hasło = dane_logowania["hasło"]
    assert UŻYTKOWNICY.get(login) != hasło