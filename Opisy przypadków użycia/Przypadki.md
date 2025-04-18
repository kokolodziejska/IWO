# Scenariusze oraz scenopisy przypadków użycia
## PU014 Edytowanie zbioru danych - Michał Jagodziński

**SCENARIUSZ GŁÓWNY**

PRE : - Zarządca danych jest zalogowany, lista zbiorów danych jest wyświetlona

1. Zarządca danych wybiera konkretny zbiór danych z listy zbiorów danych
2. System pobira dane zbioru danych
3. System wyświetla okno zbioru danych
4. Zarządca danych naciska guzik "edycja"
5. System wyświetla formularz edycji danych zbioru danych
6. Zarządca danych edytuje dane zbioru dancyh
   [Zatwierdzenie]
7. System waliduje nowe dane zbioru danych
   [Dane poprawne]
8. System wyświelta komunikat "sukces"
   
final : success

POST : Zmodyfikowane dane zbioru danych zapisane w systemie

**SCENARIUSZ ALTERNATYWNY 1 (Anulowanie)**

1.-6. tak jak w scenariuszu głównym

7a). Powrót do punktu nr 3.

final : canceled

POST : Dane zbioru danych nie zostały zmodyfikowane

**SCENARIUSZ ALTERNATYWNY 2 (Dane niepoprawne)**

1.-7. tak jak w scenariuszu głównym

8b) System wyświelta komunikat niepowodzenie

final : failure
POST : Dane zbioru danych nie zostały zmodyfikowane

**Postulaty o zmiany w słowniku dziedziny**

Brak

**Poglądowy widok okien**

![Poglądowy widok okna edycji zbioru danych](oknaPU018.png)
## PU017 Wyświetlenie szczegółów zgłoszonej uwagi - Kornelia Kołodziejska

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
