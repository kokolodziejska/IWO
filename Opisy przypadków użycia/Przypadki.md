# Scenariusze oraz scenopisy przypadków użycia

## PU001 Logowanie do systemu - Michał Bibrzycki

**SCENARIUSZ GŁÓWNY**

PRE: Użytkownik jest niezalogowany i jest zarejestrowany w sustemie oraz zna swoje <u>dane logowania</u>

1. Użytkownik wybiera opcję "zaloguj się"
2. System wyświetla formularz logowania
3. Użytkownik wprowadza <u>dane logowania</u>
4. Użytkownik wybiera opcję "zaloguj".  
[poprawny dostęp Systemu do bazy danych]
5. System waliduje <u>dane logowania</u>  
[<u>dane logowania</u> poprawne]
6. System zmienia stan użytkownika na zalogowany
7. System wyświetla menu ekranu głównego  
final: success

POST: Użytkonik jest zalogowany

**SCENARIUSZ ALTERNATYWNY 1**

1.-4. tak jak w SCENARIUSZU GŁÓWNYM  
[brak dostępu Systemu do bazy danych]  
5a. System wyświetla informację "Wystąpił błąd systemu, spróbuj ponownie później"  
final : failure

POST: Użytkonik jest niezalogowany

**SCENARIUSZ ALTERNATYWNY 2**

1.-5. tak jak w SCENARIUSZU GŁÓWNYM  
[<u>dane logowania</u> niepoprawne]  
6b. System wyświetla informację "Niepoprawne dane logowania"  
final : failure

POST: Użytkonik jest niezalogowany

**Brak zmian w słowniku dziedziny**

**Poglądowy widok okien**

![Poglądowy widok okna logowania](oknaPU001.png)

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
