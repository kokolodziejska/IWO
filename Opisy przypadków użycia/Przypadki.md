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

## PU002 Wyświetlenie listy zbiorów danych - Bartłomiej Janota

**SCENARIUSZ GŁÓWNY:**

PRE: Użytkownik uzyskał dostęp do interfejsu systemu.

1. Użytkownik wybiera zakładkę "Zbiory danych".
2. System pobiera listę dostępnych zbiorów danych.
3. System wyświetla dane w formie listy.

final: success

POST: Stan systemu się nie zmienił.

**SCENARIUSZ ALTERNATYWNY 1:**

1-3 tak jak w SCENARIUSZU GŁÓWNYM
<<invoke>> [Użytkownik klika w wybrany zbiór danych] 4. System przekierowuje użytkownika na stronę ze szczegółami tego zbioru danych.

final: success

POST: Stan systemu się nie zmienił.

**SCENARIUSZ ALTERNATYWNY 2:**

1-3 tak jak w SCENARIUSZU GŁÓWNYM
4a. Użytkownik wybiera opcje filtrowania.
5a. System wyświetla listę dostępnych zbiorów danych z zastosowanymi filtrami.

final: success

POST: Stan systemu się nie zmienił.

**SCENARIUSZ ALTERNATYWNY 3:**

1-4 tak jak w SCENARIUSZU ALTERNATYWNYM 2
[brak zbiorów pasujących do opcji filtrowania]
5a. System wyświetla komunikat o braku dostępnych zbiorów danych.

final: failure

POST: Stan systemu się nie zmienił.


**SCENARIUSZ ALTERNATYWNY 4:**

1 tak jak w SCENARIUSZU GŁÓWNYM
[brak połączenia z bazą danych]
2a. System wyświetla komunikat o problemie z połączeniem.

final: failure

POST: Stan systemu się nie zmienił.


**SCENARIUSZ ALTERNATYWNY 5:**

1 tak jak w SCENARIUSZU GŁÓWNYM
[brak zbiorów danych w bazie danych]
2a. System wyświetla komunikat o braku dostępnych zbiorów danych.

final: failure

POST: Stan systemu się nie zmienił.

**Brak zmian w słowniku dziedziny**

**Poglądowy widok okien**

![Poglądowy widok okna logowania](oknaPU002.png)


## PU003 Wyświetlenie szczegółów danych - Mikołaj Tradecki

**SCENARIUSZ GŁÓWNY**

PRE : Użytkownik znajduje się w ekranie listy zbiorów danych.

1. Użytkownik wybiera zbiór danych z listy
2. System pobiera metadane zbioru danych 
   [Poprawne połączenie z bazą danych]
3. System wyświetla ekran szczogółów zbiorów danych.

\<\<invoke\>\> [Wyświetlenie wizualizacji zbioru danych]   
\<\<invoke\>\> [Pobranie dystrybucji zbioru danych]  
\<\<invoke\>\> [Zgłoszenie uwagi do zbioru danych]  
\<\<invoke\>\> [Zasubskrybowanie zbioru danych]  
\<\<invoke\>\> [Wygenerowanie opisów bibliograficznych]   
final: success  
POST: Stan się nie zmienia   

**SCENARIUSZ ALTERNATYWNY 1**  
1-2 Tak jak w scenariuszu głównym.   
3a. System wyświetla komunikato o błędzie połączenia  
4a. Użytkownik wybiera przycisk zamknij  
final: failure  
POST: Stan się nie zmienia.  
![Poglądowe scenopisy dla przypadku użycia PU003 ](oknaPU003.png)
=======


## PU008 Zasubskrybowanie zbioru danych- Mateusz Borka

**SCENARIUSZ GŁÓWNY**

PRE: Użytkownik jest załogowany, użytkownik wyświetlil szczegóły zbioru danych.

1. Użytkownik klika przycisk "Subskrybuj".
2. System wyświetla formularz z wyborem formwy powiadomienia(e-mail/SMS).
3. Użytkownik zaznacza znakiem "X" preferowane opcje.
4. Użytkownik naciska przycisk "Potwierdź".
5. System weryfikuje punkt kontaktowy użytkownika.
[dane poprawne]
6. System dodaje użytkownika do listy subskrybentów danego zbioru danych.
final: success

POST: Użytkonik znajduje się w bazie subskrybentów danego zbioru danych.

**SCENARIUSZ ALTERNATYWNY 1(Anulowanie)**

1.-5. tak jak w SCENARIUSZU GŁÓWNYM
[dane niepoprawne]
6a. System wyświetla komunikat o błędnych danych profilu.
[anulowanie subskrybcji]
7a. Użytkownik wybiera opcję "Zamknij"
8a. System zamyka formularz z wyborem formy powiadomienia
final:failure


![image](https://github.com/user-attachments/assets/020cd40e-247a-4b24-b309-be5bc7c1e5cd)



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

![Poglądowy widok okna edycji zbioru danych](oknaPU014.png)
## PU016 Wyświetlenie zweryfikowanej listy zgłoszonych uwag - Michał Ciechan

**SCENARIUSZ GŁÓWNY**

PRE: Zarządca danych jest zalogowany

1\. Zarządca danych wybiera opcję "uwagi do rozpatrzenia".  
2\. System pobiera listę uwag do zbiorów danych ze statusem "zweryfikowana".  
3\. System wyświetla okno listy uwag do zbiorów danych.  
<\<invoke\>> [wybrano opcje "szczegóły uwagi"] PU017 Wyświetlenie szczegółów zgłoszonej uwagi.  
4\. Zarządca danych wybiera opcję "zamknij uwagi do rozpatrzenia".  

FINAL: Sukces  
POST: Brak zmian w liście uwag do zbiorów danych

**SCENARIUSZ ALTERNATYWNY 1**

1.-3. Tak jak w SCENARIUSZ GŁÓWNY.  
4a. Zarządca danych wpisuje dane filtrowania uwag do zbiorów danych.  
5a. System waliduje dane filtrowania uwag do zbiorów danych.  
[dane poprawne]  
6a. System filtruje uwagi do zbiorów danych.  
7a. Powrót do kroku 3 w SCENARIUSZ GŁÓWNY.  

**SCENARIUSZ ALTERNATYWNY 2**

1.-5a. Tak jak w SCENARIUSZ ALTERNATYWNY 1.  
[dane niepoprawne]  
6b. System wyświetla komunikat "niepoprawne dane".  
7b. Powrót do kroku 4a w SCENARIUSZ ALTERNATYWNY 1.  

**SCENOPIS**

![Scenopis PU016](oknaPU016.png)

**SŁOWNIK**

Uwaga do zbioru danych:  
\+ id: string  
\+ tytuł: string  
\+ status: Status uwagi  

Status uwagi: zgłoszona, zweryfikowana, rozpatrzona, odrzucona

Dane filtrowania uwagi do zbioru danych:  
\+ zbiór danych: Zbiór danych  
\+ od: Data  
\+ do: Data  

## PU008 Zasubskrybowanie zbioru danych – Dominika Kalinowska

**SCENARIUSZ GŁÓWNY**

**PRE**:  
- Użytkownik jest zalogowany  
- Użytkownik znajduje się w widoku szczegółów zbioru danych (PU003)  
- Zbiór danych obsługuje subskrypcje  

1. Użytkownik klika przycisk „Subskrybuj”  
2. System wyświetla okno subskrypcji z nazwą zbioru oraz wyborem kanału powiadomień  
3. Użytkownik wybiera jedną z opcji: **SMS** lub **E-mail**  
4. Użytkownik klika przycisk „Subskrybuj”  
5. System sprawdza poprawność konfiguracji wybranego kanału powiadomień  
  [Kanał skonfigurowany prawidłowo (np. podany numer, zweryfikowany mail)]
6. System zapisuje subskrypcję  
7. System wyświetla komunikat: „Zasubskrybowano pomyślnie”  

**final**: success  
**POST**: Subskrypcja została aktywowana, użytkownik będzie otrzymywał powiadomienia o aktualizacjach zbioru  

**SCENARIUSZ ALTERNATYWNY 1 (Nie wybrano kanału powiadomień)**  
3a. Użytkownik nie zaznacza żadnej opcji  
4a. System wyświetla komunikat: **„Wybór kanału powiadomień jest wymagany!”**  
**final**: failure  
**POST**: Subskrypcja nie została zapisana  

**SCENARIUSZ ALTERNATYWNY 2 (Brak danych do wybranego kanału)**  
5b. Wybrano SMS, ale numer telefonu nie jest przypisany do konta  
[System wyświetla komunikat: **„Brak numeru telefonu przypisanego do konta…”**]
**lub**  
5c. Wybrano E-mail, ale adres e-mail nie jest zweryfikowany  
[System wyświetla komunikat: **„Adres e-mail nie został zweryfikowany…”**]
**final**: failure  
**POST**: Subskrypcja nie została zapisana  

**SCENARIUSZ ALTERNATYWNY 3 (Błąd systemu)**  
6a. Wystąpił błąd systemu podczas zapisywania subskrypcji  
7a. System wyświetla okno błędu: **„Wystąpił nieoczekiwany błąd. Spróbuj ponownie później.”**  
**final**: failure  
**POST**: Subskrypcja nie została zapisana  

**Poglądowy widok okien**

![Poglądowy widok okna subskrypcji](oknaPU008.png)

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

![Poglądowe scenopisy dla przypadku użycia PU017 ](PU017.png)
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

## PU038 Przesłanie zgłoszonej uwagi do zarządcy danych - Łukasz Gumienniczuk

**SCENARIUSZ GŁÓWNY:**

PRE: Weryfikator jest zalogowany, Weryfikator ma uprawnienia do zarządzania zgłoszeniami, Weryfikator wybrał zgłoszoną uwagę

1. Weryfikator wybiera opcję "prześlij zgłoszenie uwagi".
2. System wyświetla formularz przesłania zgłoszonej uwagi.
3. Weryfikator wpisuje dodatkowe informacje uwagi.
4. Weryfikator wybiera opcję "prześlij".
5. System waliduje dodatkowe informacje uwagi.
    
    [Dane poprawne]

    6a. System zapisuje dodatkowe informacje uwagi.

    7a. System zmienia status zgłoszonej uwagi na "zweryfikowana".

    8a. Ssytem wyświetla komunikat o poprawnym przesłaniu zgłoszonej uwagi.
    
Final: success

Post: Zgłoszona uwaga została przesłana do zarządcy danych.

**SCENARIUSZ ALTERNATYWNY: [Dane niepoprawne]**

1-5. tak jak w scenariuszu głównym
        
6b. System wyświetla komunikat o niepoprawnych danych.

7b. Weryfikator wybiera opcję "ok".

Powrót do zdania 3. w scenariuszu głownym.


**SCENARIUSZ ALTERNATYWNY: [Anulowanie]**

1-3. tak jak w scenariuszu głownym

4b. Weryfikator wybiera opcję "anuluj".

5b. System wyświetla okno potwierdzenia anulowania przesłania zgłoszonej uwagi.

6b. Weryfikator wybiera opcję "ok".

Final: Failed

POST: Anulowano przesłanie zgłoszenia uwagi; nic nie zostało zmodyfikowane.

_**Dodano 'Dodatkowe Infromacje uwagi' do słownika dziedziny**_

![Okna](oknaPU038.PNG)


## PU023 Wyświetlanie listy subskrybcji - Maciej Rukat

**SCENARIUSZ GŁÓWNY**

PRE: Użytkownik jest zalogowany

1. Użytkownik wybiera opcję "moje subskrybcje"
2. System pobiera listę subskrybcji
[użytkownik ma subskrybcje]
3. System wyświetla okno listy subskrybcji<br>
 <\<invoke>> [wybrano opcję ustawienia] Edytowanie ustawień subskrybcji<br>
<\<invoke>> [wybrano opcję szczegóły] Wyświetlenie szczegółów zbioru danych
4. Użytkownik wybiera opcję "zamknij"
5. System zamyka okno listy subskrybcji<br>
final: success

POST: Stan systemu się nie zmienił

**SCENARIUSZ ALTERNATYWNY 1**

1.-2. tak jak w SCENARIUSZU GŁÓWNYM  
[użytkownik nie ma subskrybji]  
3a. System wyświetla komunikat "brak subskrybcji"  
4a. Użytkownik wybier opcję zamknij<br>
5a. System zamyka komunikat<br>
final : failure

POST: Stan systemu się nie zmienił

**SCENARIUSZ ALTERNATYWNY 2**

1.-2. tak jak w SCENARIUSZU GŁÓWNYM  
[błąd systemu]  
3b. System wyświetla komunikat "brak subskrybcji"<br>
4b. Użytkownik wybier opcję zamknij<br>
5b. System zamyka komunikat<br>
final : failure

POST: Stan systemu się nie zmienił

**Brak zmian w słowniku dziedziny**

**Poglądowy widok okien**

![Poglądowy widok okna logowania](oknaPU023.png)
=======

## PU019 Dodawanie zbioru danych - Daria Koval

### SCENARIUSZ GŁÓWNY

**PRE:** Zarządca danych jest zalogowany

| Krok | Opis |
|------|------|
| 1    | Zarządca danych wybiera opcję "Dodaj zbiór danych" |
| 2    | System wyświetla formularz dodania nowego zbioru danych |
| 3    | Zarządca danych wprowadza dane zbioru danych: <br> - identyfikator <br> - licencję dostępu <br> - opis <br> - słowa kluczowe <br> - typ/et <br> - wersję |
| 4    | System waliduje dane zbioru danych *(dane poprawne)* |
| 5    | System zapisuje zbiór danych |
| 6    | System wyświetla potwierdzenie dodania zbioru danych |

**Final:** success  

**POST:** Nowo dodany zbiór danych znajduje się w bazie zbiorów danych

---

### SCENARIUSZ ALTERNATYWNY 1 (dane niepoprawne)

| Krok | Opis |
|------|------|
| 1–4  | Jak w scenariuszu głównym *(dane niepoprawne)* |
| 5a   | System wyświetla komunikat o błędnych danych |
| 6a   | Zarządca danych wybiera opcję "Zamknij" |
| 7a   | System zamyka formularz dodania |

**Final:** failure  
**POST:** Zbiór danych nie znajduje się w bazie zbiorów danych

---
### SCENARIUSZ ALTERNATYWNY 2 (poprawa danych)
| Krok | Opis |
|------|------|
| 1–5a | Jak w Scenariuszu Alternatywnym 1 |
| 6b   | Zarządca danych wybiera opcję "Popraw" |
| 7b   | System wyświetla komunikat o wznowieniu dodania |

**Powrót do punktu 3 scenariusza głównego**
---
### SCENARIUSZ ALTERNATYWNY 3 (błąd systemu)
| Krok | Opis |
|------|------|
| 1–4  | Jak w scenariuszu głównym |
| 5c   | System wyświetla komunikat o błędzie systemu |
| 6c   | Zarządca danych wybiera opcję "Zamknij" |
| 7c   | System zamyka formularz dodania |

**Final:** failure  
**POST:** Zbiór danych nie znajduje się w bazie zbiorów danych

---
### Poglądowy widok okna

![Poglądowy widok formularza dodania zbioru danych](oknaPU013.png)


=======
## PU015 Usunięcie zbioru danych - Mikołaj Frączek

# SCENARIUSZ GŁÓWNY

**PRE**: Zarządca danych jest zalogowany

[zarządca ma uprawnienia do usunięcia zbioru danych]
1. Zarządca danych wybiera opcję "usuń zbiór danych"   
3. System wyświetla komunikat z prośbą o potwierdzenie usunięcia zbioru  
4. Zarządca danych wybiera opcję "Potwierdzam"
4. System sprawdza, czy zbiór może zostać usunięty  
[zbiór może zostać usunięty]
5. System usuwa zbiór  
6. System wyświetla komunikat o pomyślnym usunięciu zbioru  

**final**: success

**POST**: Zbiór został usunięty z systemu

---

# SCENARIUSZ ALTERNATYWNY 1

**1.-5.** tak jak w SCENARIUSZU GŁÓWNYM  
[Zbiór danych jest blokowany]
**6a.** System wyświetla komunikat: "Zbiór danych nie może zostać usunięty"

**final**: failure

**POST**: Zbiór nie został usunięty z systemu

![okna](PU015.png)

