# Formalne Wymagania Jakościowe Systemu Zarządzania Danymi Publicznymi

Poniższy dokument zawiera zestaw wymagań jakościowych, w których każda fiszka zawiera:
- **Typ** – kategoria wymagania,
- **Priorytet** – poziom ważności,
- **Trudność** – oszacowanie trudności realizacji,
- **Sposób pomiaru** – opis procedury testowej,
- **Oczekiwane wartość** – kryteria akceptacji.

---

## 1. Efektywność wydajnościowa

#### (CJU0001) Wyszukiwanie zbiorów danych przy typowym obciążeniu

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Efektywność wydajnościowa*                                                                                            |
| **Priorytet**        | *Średni*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Wykonanie testów obciążeniowych (np. za pomocą JMeter) na próbie 1000 operacji wyszukiwania, przy użyciu oprogramowania pomiarowego (dokładność 0,01 sekundy). |
| **Oczekiwane wartość** | Średni czas wyszukiwania ≤ 0,5 sekundy; odchylenie standardowe ≤ 0,1 sekundy.                                             |

---

#### (CJU0002) Wyszukiwanie zbiorów danych przy maksymalnym obciążeniu

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Efektywność wydajnościowa*                                                                                            |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Wysoka*                                                                                                               |
| **Sposób pomiaru**   | Testy wydajnościowe symulujące 100 000 równoczesnych użytkowników (np. przy użyciu Gatling) oraz 100 prób przy różnych poziomach obciążenia. |
| **Oczekiwane wartość** | Średni czas wyszukiwania ≤ 3 sekundy przy maksymalnym obciążeniu; najgorszy wynik nie przekracza 5 sekund.                 |

---

#### (CJU0003) Obsługa zapytań na sekundę

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Efektywność wydajnościowa*                                                                                            |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Wysoka*                                                                                                               |
| **Sposób pomiaru**   | Przeprowadzenie testów obciążeniowych, mierzenie liczby zapytań przetwarzanych na sekundę przy użyciu narzędzia (np. Apache JMeter). |
| **Oczekiwane wartość** | System przetwarza minimum 300 zapytań na sekundę, przy zachowaniu stabilności (300–320 zapytań/s).                         |

---

## 2. Kompatybilność

#### (CJU0004) Integracja z systemem CKAN

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Kompatybilność*                                                                                                       |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Wysoka*                                                                                                               |
| **Sposób pomiaru**   | Przeprowadzenie testów integracyjnych – weryfikacja mapowania danych oraz wymiany metadanych przez API CKAN, przy użyciu testów automatycznych. |
| **Oczekiwane wartość** | 100% zgodności przesyłu metadanych ze specyfikacją CKAN; brak błędów mapowania w 100% przypadków.                         |

---
#### (CJU0005) Kompatybilność z popularnymi przeglądarkami internetowymi

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Kompatybilność*                                                                                                       |
| **Priorytet**        | *Średni*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                            |
| **Sposób pomiaru**   | Przeprowadzenie testów kompatybilności przy użyciu narzędzi automatycznych (np. Selenium) na przeglądarkach: Chrome, Firefox, Edge oraz Safari. |
| **Oczekiwane wartość** | 95% lub więcej przypadków testowych wykonanych poprawnie we wszystkich wymienionych przeglądarkach.                      |

---
## 3. Użyteczność

#### (CJU0005) Intuicyjny interfejs z kontekstowymi podpowiedziami

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Użyteczność*                                                                                                          |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Przeprowadzenie testów użyteczności z udziałem minimum 15 użytkowników oraz ankietowanie intuicyjności na skali 1–10.      |
| **Oczekiwane wartość** | Średnia ocena intuicyjności ≥ 8; czas nauki podstawowych funkcji ≤ 5 minut.                                             |

---

#### (CJU0006) Szybkie dodawanie nowego zbioru danych

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Użyteczność*                                                                                                          |
| **Priorytet**        | *Średni*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Testy użyteczności – pomiar czasu dodania nowego zbioru danych przez 10 użytkowników wykonujących ustalony scenariusz.    |
| **Oczekiwane wartość** | Średni czas dodania zbioru danych ≤ 1 minuta; najgorszy wynik nie przekracza 1,5 minuty.                                  |

---

#### (CJU0007) Obsługa skrótów klawiszowych

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Użyteczność*                                                                                                          |
| **Priorytet**        | *Średni*                                                                                                               |
| **Trudność**         | *Niska*                                                                                                                |
| **Sposób pomiaru**   | Testy funkcjonalne – pomiar liczby operacji wykonanych przy użyciu skrótów w porównaniu z nawigacją tradycyjną, wraz z rejestracją czasu. |
| **Oczekiwane wartość** | Skróty skracają czas wykonania operacji o co najmniej 20% w porównaniu do nawigacji; liczba błędów związanych ze skrótami ≤ 2 na 100 operacji. |

---
