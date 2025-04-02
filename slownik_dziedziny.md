# Słownik dziedziny

## 1. **Zbiór danych**

**Opis:**
Zestaw powiązanych ze sobą informacji.

**Atrybuty:**

* `identyfikator: string`
* `licencja dostępu: Licencja` (enum)
* `modyfikacje: Data [0..*]`
* `opis: string [1..*]`
* `słowa kluczowe: list<string>`
* `tytul: string [1..*]`
* `wersja: int`

---

## 2. **Punkt kontaktowy**

**Opis:**
Dane osoby lub organizacji kontaktowej.

**Atrybuty:**

* `adres: string`
* `email: string`
* `nazwa: string`
* `telefon: string`

---

## 3. **Dystrybucja danych**

**Opis:**
Konkretna forma udostępnienia zbioru danych.

**Atrybuty:**

* `format: Format` (enum)
* `opis: string [1..*]`
* `tytul: string [1..*]`
* `url: string`

---

## 4. **Schemat danych**

**Opis:**
Definicja struktury zbioru danych.

**Atrybuty:**

* `nazwa: string`
* `opis: string`
* `struktura: string [1..*]`
* `wersja: int`

---

## 5. **Uwaga do zbioru danych**

**Opis:**
Komentarz lub sugestia dotycząca zbioru danych.

**Atrybuty:**

* `data: Data`
* `dystrybucja: Format` (enum)
* `tekst: string`

---

## 6. **Użytkownik**

**Opis:**
Osoba lub system korzystający z portalu.

**Atrybuty:**

* `imie: string [0..1]`
* `nazwisko: string [0..1]`

---

## 7. **Parametry wizualizacji**

**Opis:**
Ustawienia konfigurujące wizualizację danych.

**Atrybuty:**

* `motyw: motyw` (enum)
* `zakres danych: Zakres danych` (enum)

---

## 8. **Subskrypcja**

**Opis:**
Mechanizm powiadamiania o zmianach w zbiorze danych.

**Atrybuty:**

* `częstotliwość: int`
* `typ zmiany: typ zmiany` (enum)

---

## 9. **Powiadomienie**

**Opis:**
Informacja wysyłana w ramach subskrypcji.

**Atrybuty:**

* `data: Data`

---

## 10. **Wizualizacja**

**Opis:**
Definicja sposobu graficznej prezentacji danych.

**Atrybuty:**

* `rodzaj wizualizacji: Rodzaj wizualizacji` (enum)

---

## 11. **Dane Logowania**

**Opis:**
Dane uwierzytelniające użytkownika.

**Atrybuty:**

* `email: string`
* `haslo: string`
* `nazwa użytkownika: string`

---

## 12. **Typy Danych i Wyliczeniowe**

* **`Data` (DataType):** Struktura przechowująca: `Dzien: int`, `Godzina: int`, `Miesiac: int`, `Minuta: int`, `Rok: int`, `Sekunda: int`.
* **`Rodzaj wizualizacji` (Enum):** `Wykres`, `Tekst`, `Zdjęcie`, `Tabela`.
* **`typ zmiany` (Enum):** `nowa wersja`, `zmiana licencji`, `zmiana w punktach kontaktowych`, `zmiana danych`, `zmiana metadanych zbioru`.
* **`Zakres danych` (Enum):** `Czasowy`, `Geograficzny`.
* **`motyw` (Enum):** `jasny`, `ciemny`.
* **`Format` (Enum):** `csv`, `json`, `xml`, `api`, `xlsx`,`api`.
* **`Licencja` (Enum):** `Publiczna`, `Niepubliczna`.

---