# Scenariusze oraz scenopisy przypadków użycia

## PU017 Wyświetlenie szczegółów zgłoszonej uwagi - Kornelia Kołodziejska

**SCENARIUSZ GŁÓWNY**

PRE : -Zarządca danych jest zalogowany

1. Zarządca danych wybiera opcję "wyświetl szczegóły zgłoszonej uwagi".
2. System pobiera szczegóły zgłoszonej uwagi. [dane pobrane prawidłowo].
3. System wyświetla szczegóły uwagi.

POST : Stan systemu bez zmian

**SCENARIUSZ ALTERNATYWNY 1 (błąd pobrania danych)**

PRE : -Zarządca danych jest zalogowany

1. Zarządca danych wybiera opcję "wyświetl szczegóły zgłoszonej uwagi".
2. System pobiera szczegóły zgłoszonej uwagi. [dane pobrane nieprawidłowo]
3. System wyświetla okno komunikatu "Błąd pobrania danych".

POST : Stan systemu bez zmian

**Zmiany w słowniku dziedziny**

Szczegóły zgłoszonej uwagi: Zawierają datę, nazwę użytkownika, status uwagi, treść uwagi, nazwę zbioru, którego dotyczy uwaga.

**Scenopisy do przypadku użycia**

![Poglądowy widok okna zmiany statusu uwagi](PU017.png)
## PU018 Zmiana statusu zgłoszonej uwagi do zbioru - Jakub Klenkiewicz

**SCENARIUSZ GŁÓWNY**

PRE : - Okno szczegółów uwagi do zbioru zostało poprawnie wyświetlone

1. Zarządca danych klika na przycisk “zmień”
2. System wyświetla formularz zmiany statusu uwagi do zbioru
3. Zarządca danych wybiera status uwagi do zbioru (rozpatrzona/nierozpatrzona)
4. Zarządca danych naciska przycisk zatwierdź
5. System aktualizuje status uwagi do zbioru
6. System zapisuje informacje o zmianie statusu uwagi do zbioru do historii działań
7. System wyświetla okno pomyślnej zmiany statusu uwagi do zbioru
8. Zarządca danych naciska przycisk ok

final : success

POST : Status uwagi do zbioru danych został zmieniony na pożądany, oraz zmiana ta została zapisana do historii działań

**SCENARIUSZ ALTERNATYWNY 1 (niepowodzenie połączenia z bazą danych)**

1.-4. tak jak w scenariuszu głównym

5a). System niepomyślnie próbuje połączyć się z bazą danych zawierającą status uwagi

6a). System wyświetla okno niepomyślnej zmiany statusu uwagi do zbioru wraz z powodem

7a). Zarządca danych naciska przycisk ok

final : failure

POST : Status uwagi do zbioru danych nie został zaktualizowany

**SCENARIUSZ ALTERNATYWNY 2 (anulowanie)**

1.-2. tak jak w scenariuszu głównym

3b) Zarządca danych naciska przycisk "anuluj"

4b) System zamyka formularz zmiany statusu uwagi do zbioru.

final**:** canceled
POST**:** Status uwagi do zbioru danych nie został zmieniony. Żadna informacja nie została zapisana do historii działań.

**Postulaty o zmiany w słowniku dziedziny**

- Dodać status uwagi jako atrybut uwagi do zbioru danych → enum : rozpatrzona/nierozpatrzona

**Poglądowy widok okien**

![Poglądowy widok okna zmiany statusu uwagi](oknaPU018.png)
