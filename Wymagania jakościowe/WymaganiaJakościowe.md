# Formalne Wymagania Jakościowe Systemu Zarządzania Danymi Publicznymi

Poniższy dokument zawiera zestaw wymagań jakościowych, w których każda fiszka zawiera:
- **Typ** – kategoria wymagania,
- **Priorytet** – poziom ważności,
- **Trudność** – oszacowanie trudności realizacji,
- **Sposób pomiaru** – opis procedury testowej,
- **Oczekiwana wartość** – kryteria akceptacji.

---

## 1. Efektywność wydajnościowa

#### (J0001) Wyszukiwanie zbiorów danych przy typowym obciążeniu

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Efektywność wydajnościowa*                                                                                            |
| **Priorytet**        | *Średni*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Wykonanie testów obciążeniowych (np. za pomocą JMeter) na próbie 1000 operacji wyszukiwania, przy użyciu oprogramowania pomiarowego (dokładność 0,01 sekundy). |
| **Oczekiwana wartość** | Średni czas wyszukiwania ≤ 0,5 sekundy; odchylenie standardowe ≤ 0,1 sekundy.                                             |

---

#### (J0002) Wyszukiwanie zbiorów danych przy maksymalnym obciążeniu

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Efektywność wydajnościowa*                                                                                            |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Wysoka*                                                                                                               |
| **Sposób pomiaru**   | Testy wydajnościowe symulujące 100 000 równoczesnych użytkowników (np. przy użyciu Gatling) oraz 100 prób przy różnych poziomach obciążenia. |
| **Oczekiwana wartość** | Średni czas wyszukiwania ≤ 3 sekundy przy maksymalnym obciążeniu; najgorszy wynik nie przekracza 5 sekund.                 |

---

#### (J0003) Obsługa zapytań na sekundę

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Efektywność wydajnościowa*                                                                                            |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Wysoka*                                                                                                               |
| **Sposób pomiaru**   | Przeprowadzenie testów obciążeniowych, mierzenie liczby zapytań przetwarzanych na sekundę przy użyciu narzędzia (np. Apache JMeter). |
| **Oczekiwana wartość** | System przetwarza minimum 300 zapytań na sekundę, przy zachowaniu stabilności (300–320 zapytań/s).                         |

---

## 2. Kompatybilność

#### (J0004) Integracja z systemem CKAN

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Kompatybilność*                                                                                                       |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Wysoka*                                                                                                               |
| **Sposób pomiaru**   | Przeprowadzenie testów integracyjnych – weryfikacja mapowania danych oraz wymiany metadanych przez API CKAN, przy użyciu testów automatycznych. |
| **Oczekiwana wartość** | 100% zgodności przesyłu metadanych ze specyfikacją CKAN; brak błędów mapowania w 100% przypadków.                         |

---
#### (J0005) Kompatybilność z popularnymi przeglądarkami internetowymi

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Kompatybilność*                                                                                                       |
| **Priorytet**        | *Średni*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                            |
| **Sposób pomiaru**   | Przeprowadzenie testów kompatybilności przy użyciu narzędzi automatycznych (np. Selenium) na przeglądarkach: Chrome, Firefox, Edge oraz Safari. |
| **Oczekiwana wartość** | 95% lub więcej przypadków testowych wykonanych poprawnie we wszystkich wymienionych przeglądarkach.                      |

---
## 3. Użyteczność

#### (J0006) Intuicyjny interfejs z kontekstowymi podpowiedziami

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Użyteczność*                                                                                                          |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Przeprowadzenie testów użyteczności z udziałem minimum 15 użytkowników oraz ankietowanie intuicyjności na skali 1–10.      |
| **Oczekiwana wartość** | Średnia ocena intuicyjności ≥ 8; czas nauki podstawowych funkcji ≤ 5 minut.                                             |

---

#### (J0007) Szybkie dodawanie nowego zbioru danych

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Użyteczność*                                                                                                          |
| **Priorytet**        | *Średni*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Testy użyteczności – pomiar czasu dodania nowego zbioru danych przez 10 użytkowników wykonujących ustalony scenariusz.    |
| **Oczekiwana wartość** | Średni czas dodania zbioru danych ≤ 1 minuta; najgorszy wynik nie przekracza 1,5 minuty.                                  |

---

#### (J0008) Obsługa skrótów klawiszowych

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Użyteczność*                                                                                                          |
| **Priorytet**        | *Średni*                                                                                                               |
| **Trudność**         | *Niska*                                                                                                                |
| **Sposób pomiaru**   | Testy funkcjonalne – pomiar liczby operacji wykonanych przy użyciu skrótów w porównaniu z nawigacją tradycyjną, wraz z rejestracją czasu. |
| **Oczekiwana wartość** | Skróty skracają czas wykonania operacji o co najmniej 20% w porównaniu do nawigacji; liczba błędów związanych ze skrótami ≤ 2 na 100 operacji. |

---
## 4. Niezawodność

#### (J0009) Wysoka dostępność systemu

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Niezawodność*                                                                                                         |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Wysoka*                                                                                                               |
| **Sposób pomiaru**   | Monitorowanie systemu przy użyciu narzędzi do pomiaru uptime (np. UptimeRobot) przez okres minimum 1 miesiąca w środowisku produkcyjnym. |
| **Oczekiwana wartość** | Uptime ≥ 98% (nie więcej niż 14 godzin i 24 minut niedostępności miesięcznie).                                                   |

---

#### (J0010) Automatyczne przełączenie na zapasowy serwer w razie awarii

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Niezawodność*                                                                                                         |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                               |
| **Sposób pomiaru**   | Symulacja awarii głównego serwera w środowisku testowym z monitorowaniem czasu od wykrycia awarii do pełnego przywrócenia działania usług na serwerze zapasowym. |
| **Oczekiwana wartość** | System automatycznie przełącza się na zapasowy serwer w czasie nie dłuższym niż 10 minut; brak utraty danych i konieczności interwencji użytkownika.                                                   |

---

#### (J0011) Stabilność działania przez długi okres

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Niezawodność*                                                                                                         |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Wysoka*                                                                                                               |
| **Sposób pomiaru**   | Symulacja ciągłego działania systemu w środowisku testowym przez 30 dni przy rzeczywistym obciążeniu.                    |
| **Oczekiwana wartość** | Brak restartów systemu; liczba krytycznych błędów ≤ 1 na 30 dni.                                                       |

---


#### (J0012) Automatyczne kopie zapasowe i przywracanie danych

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Niezawodność*                                                                                                         |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Symulacja awarii i test przywracania danych, mierzenie czasu od inicjacji przywracania do pełnej operacyjności systemu.   |
| **Oczekiwana wartość** | Kopie zapasowe tworzone co 12 godzin; czas przywracania ≤ 10 minut; utrata danych nie przekracza 2 minut operacyjnego czasu. |

---

## 5. Bezpieczeństwo

#### (J0013) Definicja ról i uprawnień

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Bezpieczeństwo*                                                                                                       |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Audyt bezpieczeństwa oraz testy penetracyjne skoncentrowane na kontroli dostępu, weryfikacja polityki ról przy użyciu narzędzi audytowych. |
| **Oczekiwana wartość** | 100% zgodność z założeniami polityki dostępu; brak możliwości nieautoryzowanego dostępu.                                 |

---

#### (J0014) Prowadzenie dziennika zdarzeń

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Bezpieczeństwo*                                                                                                       |
| **Priorytet**        | *Kluczowy*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Testy audytowe – symulacja operacji, a następnie próba modyfikacji dziennika przy użyciu sum kontrolnych i mechanizmów zabezpieczających. |
| **Oczekiwana wartość** | Każda operacja jest niezmiennie zapisywana; wszelkie próby modyfikacji kończą się niepowodzeniem.                      |

---

## 6. Łatwość utrzymania

#### (J0015) Niezależne wdrażanie i aktualizowanie modułów

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Łatwość utrzymania*                                                                                                   |
| **Priorytet**        | *Średni*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Audyt architektury systemu przeprowadzony przez niezależnych ekspertów. Weryfikacja, czy wdrożenie nowej wersji modułu nie wymaga restartu ani modyfikacji innych komponentów. |
| **Oczekiwana wartość** | Ocena ekspercka ≥ 90% zgodności z wymaganiami modułowości; możliwość wdrażania i aktualizowania pojedynczych modułów bez wpływu na działanie pozostałych części systemu.      |

---

#### (J0016) Reużywalność komponentów

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Łatwość utrzymania*                                                                                                   |
| **Priorytet**        | *Średni*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Audyt kodu źródłowego – ocena stopnia niezależności oraz stopnia zależności od kontekstu systemowego. |
| **Oczekiwana wartość** | Ocena ekspercka ≥ 90% zgodności z wymaganiami modułowości.      |

---

#### (J0017) Testowalność krytycznych funkcji

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Łatwość utrzymania*                                                                                                   |
| **Priorytet**        | *Średni*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Wykorzystanie narzędzi do analizy pokrycia kodu (np. SonarQube) oraz pomiar czasu wykonania pełnego zestawu testów automatycznych. |
| **Oczekiwana wartość** | Pokrycie krytycznych funkcji = 100%; czas wykonania testów ≤ 5 minut.                                                    |

---

## 7. Przenośność

#### (J0018) Uruchomienie systemu na różnych systemach operacyjnych

|                        |                                                                                                                       |
| ---------------------: | :-------------------------------------------------------------------------------------------------------------------- |
| **Typ**              | *Przenośność*                                                                                                          |
| **Priorytet**        | *Średni*                                                                                                             |
| **Trudność**         | *Średnia*                                                                                                              |
| **Sposób pomiaru**   | Testy instalacyjne przeprowadzone na systemach macOS, Windows oraz Linux przy użyciu automatycznych skryptów instalacyjnych oraz manualna weryfikacja funkcjonalności. |
| **Oczekiwana wartość** | System uruchamia się bez modyfikacji kodu źródłowego na wszystkich trzech platformach; funkcjonalność identyczna (zgodność 100%). |
