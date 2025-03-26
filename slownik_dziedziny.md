# Słownik Dziedziny

## 1. **Zbiór danych**

**Opis:**  
Zestaw informacji o wspólnych cechach (np. temat, pochodzenie), który może być wersjonowany i udostępniany w różnych formatach.

**Atrybuty:**

- `identyfikator` – unikalny numer lub kod wskazujący zbiór danych.
- `wersja` – oznaczenie wersji (np. 1.0, 1.1), pozwalające identyfikować konkretne zmiany.
- `opis` – krótki opis zawartości i zastosowania zbioru danych.
- `słowa kluczowe` – terminy pomagające w wyszukiwaniu zbioru.
- `punkty kontaktowe` – informacje kontaktowe odpowiedzialnych osób lub instytucji.
- `licencja dostępu` – zasady korzystania (np. otwarta, komercyjna, wymaga zgody).

---

## 2. **Punkt kontaktowy**

**Opis:**  
Dane osoby lub organizacji odpowiedzialnej za zbiór danych lub inną część systemu.

**Atrybuty:**

- `nazwa` – imię i nazwisko, dział lub firma.
- `email` – adres e-mail.
- `telefon` – numer telefonu.
- `adres` – fizyczny adres (ulica, kod pocztowy, miasto).

---

## 3. **Dystrybucja danych**

**Opis:**  
Sposób udostępnienia zbioru danych (np. plik do pobrania, API).

**Atrybuty:**

- `format` – typ pliku lub formatu (CSV, JSON, XML).
- `url` – adres do pobrania lub przeglądania danych.

---

## 4. **Schemat danych**

**Opis:**  
Definicja struktury zbioru danych — opis pól, ich nazw i typów.

**Atrybuty:**

- `opis pól` – szczegóły każdego pola (nazwa, typ, wymagalność).

---

## 5. **Uwaga do zbioru danych**

**Opis:**  
Komentarz lub sugestia zgłoszona do danego zbioru (np. błędy, propozycje zmian).

**Atrybuty:**

- `tekst` – treść uwagi.
- `data` – data zgłoszenia (dzień, miesiąc, rok).
- `użytkownik` – osoba zgłaszająca uwagę.
- `zbiór danych` – odniesienie do konkretnego zbioru danych.
- `dystrybucja` _(opcjonalnie)_ – jeżeli uwaga dotyczy konkretnej dystrybucji.

---

## 6. **Użytkownik**

**Opis:**  
Osoba korzystająca z systemu – może się rejestrować, logować, pobierać dane, zgłaszać uwagi itp.

**Atrybuty:**

- `imię` – imię użytkownika.
- `nazwisko` – nazwisko użytkownika.
- `punkty kontaktowe` – dane kontaktowe użytkownika.

---

## 7. **Parametry wizualizacji**

**Opis:**  
Ustawienia prezentacji danych dla użytkownika.

**Atrybuty (przykładowe):**

- `rodzaj wizualizacji` – typ wykresu (np. słupkowy, liniowy).
- `zakres danych` – część danych objęta wizualizacją.
- `motyw` – styl prezentacji (np. jasny / ciemny).
- `skalowanie` – sposób filtrowania lub skalowania danych.

---

## 8. **Subskrypcja**

**Opis:**  
Mechanizm powiązania użytkownika z danym zbiorem danych w celu otrzymywania powiadomień o zmianach.

**Atrybuty:**

- `zbiór danych` – zbiór objęty subskrypcją.
- `użytkownik` – użytkownik subskrybujący zbiór.
- `częstotliwość` – jak często są wysyłane powiadomienia (np. natychmiast, raz dziennie).
- `typ zmiany` – rodzaj zmian wywołujących powiadomienie (np. nowa wersja, zmiana licencji).

---

## 9. **Powiadomienie**

**Opis:**  
Informacja wysyłana do użytkownika w ramach subskrypcji.

**Atrybuty:**

- `subskrypcja` – źródło powiadomienia.
- `data` – data/godzina wysłania powiadomienia.

---
