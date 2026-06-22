Feature: Logowanie użytkownika

  Scenario: Pomyślne logowanie
    Given użytkownik podaje login "admin@test.com" i hasło "Admin123"
    When system sprawdza dane
    Then użytkownik zostaje zalogowany

  Scenario: Błędne hasło
    Given użytkownik podaje login "admin@test.com" i hasło "złehasło"
    When system sprawdza dane
    Then użytkownik widzi błąd "Nieprawidłowe dane logowania"