# Formalne Wymagania Jakościowe Systemu Zarządzania Danymi Publicznymi

Poniższy dokument zawiera zestaw wymagań jakościowych, w których każda fiszka zawiera:
- **Typ** – kategoria wymagania,
- **Priorytet** – poziom ważności,
- **Trudność** – oszacowanie trudności realizacji,
- **Sposób pomiaru** – opis procedury testowej,
- **Oczekiwane wartość** – kryteria akceptacji.

---

#### (J0001) Wyszukiwanie zbiorów danych przy typowym obciążeniu

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Efektywność wydajnościowa*                                                                                                                 |
| **Priorytet**          | *Średni*                                                                                                                                  |
| **Trudność**           | *Średnia*                                                                                                                                 |
| **Sposób pomiaru**     | Wykonanie testów obciążeniowych (np. za pomocą JMeter) na próbie 1000 operacji wyszukiwania, przy użyciu oprogramowania pomiarowego (dokładność 0,01 sekundy). |
| **Oczekiwane wartość** | Średni czas wyszukiwania ≤ 0,5 sekundy; odchylenie standardowe ≤ 0,1 sekundy.                                                              |

---

#### (J0002) Wyszukiwanie zbiorów danych przy maksymalnym obciążeniu

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Efektywność wydajnościowa*                                                                                                                 |
| **Priorytet**          | *Kluczowy*                                                                                                                                |
| **Trudność**           | *Wysoka*                                                                                                                                  |
| **Sposób pomiaru**     | Testy wydajnościowe symulujące 100 000 równoczesnych użytkowników (np. przy użyciu Gatling) oraz 100 prób przy różnych poziomach obciążenia. |
| **Oczekiwane wartość** | Średni czas wyszukiwania ≤ 3 sekundy przy maksymalnym obciążeniu; najgorszy wynik nie przekracza 5 sekund.                                   |

---

#### (J0003) Obsługa zapytań na sekundę

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Efektywność wydajnościowa*                                                                                                                 |
| **Priorytet**          | *Kluczowy*                                                                                                                                |
| **Trudność**           | *Wysoka*                                                                                                                                  |
| **Sposób pomiaru**     | Przeprowadzenie testów obciążeniowych, mierzenie liczby zapytań przetwarzanych na sekundę przy użyciu narzędzia (np. Apache JMeter).        |
| **Oczekiwane wartość** | System przetwarza minimum 300 zapytań na sekundę, przy zachowaniu stabilności (300–320 zapytań/s).                                           |

---

#### (J0004) Minimalizacja zużycia zasobów serwera

|                        |                                                                                                                  |
| ---------------------: | ---------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Efektywność wydajnościowa*                                                                                       |
| **Priorytet**          | *Niski*                                                                                                          |
| **Trudność**           | *Średnia*                                                                                                        |
| **Sposób pomiaru**     | Monitoring zasobów serwera przy symulacji 50 000 jednoczesnych użytkowników.                                      |
| **Oczekiwane wartość** | Zużycie CPU poniżej 50%, zużycie RAM poniżej 70%.                                                                  |

---

#### (J0005) Integracja z systemem CKAN

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Kompatybilność*                                                                                                                          |
| **Priorytet**          | *Kluczowy*                                                                                                                                |
| **Trudność**           | *Wysoka*                                                                                                                                  |
| **Sposób pomiaru**     | Przeprowadzenie testów integracyjnych – weryfikacja mapowania danych oraz wymiany metadanych przez API CKAN, przy użyciu testów automatycznych. |
| **Oczekiwane wartość** | 100% zgodności przesyłu metadanych ze specyfikacją CKAN; brak błędów mapowania w 100% przypadków.                                            |

---

#### (J0006) Kompatybilność z popularnymi przeglądarkami internetowymi

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Kompatybilność*                                                                                                                          |
| **Priorytet**          | *Średni*                                                                                                                                  |
| **Trudność**           | *Średnia*                                                                                                                               |
| **Sposób pomiaru**     | Przeprowadzenie testów kompatybilności przy użyciu narzędzi automatycznych (np. Selenium) na przeglądarkach: Chrome, Firefox, Edge oraz Safari. |
| **Oczekiwane wartość** | 95% lub więcej przypadków testowych wykonanych poprawnie we wszystkich wymienionych przeglądarkach.                                         |

---

#### (J0007) Kompatybilność z systemem CEPiK

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Kompatybilność*                                                                                                                          |
| **Priorytet**          | *Średni*                                                                                                                                  |
| **Trudność**           | *Wysoka*                                                                                                                                  |
| **Sposób pomiaru**     | Testy integracyjne z API systemu CEPiK, weryfikacja przesyłu danych oraz rejestracji pojazdów przy różnych poziomach obciążenia.              |
| **Oczekiwane wartość** | 98% poprawności przesyłu danych przy przepustowości zgodnej z wymaganiami API CEPiK.                                                       |

---

#### (J0008) Intuicyjny interfejs z kontekstowymi podpowiedziami

|                        |                                                                                                           |
| ---------------------: | :--------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Użyteczność*                                                                                             |
| **Priorytet**          | *Kluczowy*                                                                                                |
| **Trudność**           | *Średnia*                                                                                                 |
| **Sposób pomiaru**     | Ankieta SUS przeprowadzona po zakończeniu sesji testowej z użytkownikami.                                   |
| **Oczekiwane wartość** | Wynik powyżej 90 punktów.                                                                                   |

---

#### (J0009) Dostępność zgodna z WCAG 2.1 (AA)

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Użyteczność*                                                                                                                             |
| **Priorytet**          | *Kluczowy*                                                                                                                                |
| **Trudność**           | *Wysoka*                                                                                                                                  |
| **Sposób pomiaru**     | Audyt dostępności z wykorzystaniem narzędzi automatycznych oraz audytu eksperckiego.                                                       |
| **Oczekiwane wartość** | 100% zgodności z poziomem AA.                                                                                                               |

---

#### (J0010) Szybkie dodawanie nowego zbioru danych

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Użyteczność*                                                                                                                             |
| **Priorytet**          | *Średni*                                                                                                                                  |
| **Trudność**           | *Średnia*                                                                                                                               |
| **Sposób pomiaru**     | Testy użyteczności – pomiar czasu dodania nowego zbioru danych przez 10 użytkowników wykonujących ustalony scenariusz.                       |
| **Oczekiwane wartość** | Średni czas dodania zbioru danych ≤ 1 minuta; najgorszy wynik nie przekracza 1,5 minuty.                                                    |

---

#### (J0011) Obsługa skrótów klawiszowych

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Użyteczność*                                                                                                                             |
| **Priorytet**          | *Średni*                                                                                                                                  |
| **Trudność**           | *Niska*                                                                                                                                   |
| **Sposób pomiaru**     | Testy funkcjonalne – pomiar liczby operacji wykonanych przy użyciu skrótów w porównaniu z nawigacją tradycyjną, wraz z rejestracją czasu.  |
| **Oczekiwane wartość** | Skróty skracają czas wykonania operacji o co najmniej 20% w porównaniu do nawigacji; liczba błędów związanych ze skrótami ≤ 2 na 100 operacji. |

---

#### (J0012) Czytelność powiadomień

|                        |                                                                                                                                          |
| ---------------------: | :--------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Użyteczność*                                                                                                                            |
| **Priorytet**          | *Kluczowy*                                                                                                                               |
| **Trudność**           | *Średnia*                                                                                                                                |
| **Sposób pomiaru**     | Ankieta przeprowadzona wśród użytkowników, oceniająca przejrzystość i zrozumiałość powiadomień.                                            |
| **Oczekiwane wartość** | Średni wynik ankiety ≥ 95%.                                                                                                                |

---

#### (J0013) Wysoka dostępność systemu

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Niezawodność*                                                                                                                            |
| **Priorytet**          | *Kluczowy*                                                                                                                                |
| **Trudność**           | *Wysoka*                                                                                                                                  |
| **Sposób pomiaru**     | Monitorowanie systemu przy użyciu narzędzi do pomiaru uptime (np. UptimeRobot) przez okres minimum 1 miesiąca w środowisku produkcyjnym.     |
| **Oczekiwane wartość** | Uptime ≥ 99,9% (nie więcej niż 43 minuty niedostępności miesięcznie).                                                                     |

---

#### (J0014) Stabilność działania przez długi okres

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Niezawodność*                                                                                                                            |
| **Priorytet**          | *Kluczowy*                                                                                                                                |
| **Trudność**           | *Wysoka*                                                                                                                                  |
| **Sposób pomiaru**     | Symulacja ciągłego działania systemu w środowisku testowym przez 30 dni przy rzeczywistym obciążeniu.                                         |
| **Oczekiwane wartość** | Brak restartów systemu; liczba krytycznych błędów ≤ 1 na 30 dni.                                                                            |

---

#### (J0015) Automatyczne kopie zapasowe i przywracanie danych

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Niezawodność*                                                                                                                            |
| **Priorytet**          | *Kluczowy*                                                                                                                                |
| **Trudność**           | *Średnia*                                                                                                                               |
| **Sposób pomiaru**     | Symulacja awarii i test przywracania danych, mierzenie czasu od inicjacji przywracania do pełnej operacyjności systemu.                        |
| **Oczekiwane wartość** | Kopie zapasowe tworzone co 12 godzin; czas przywracania ≤ 10 minut; utrata danych nie przekracza 2 minut operacyjnego czasu.                  |

---

#### (J0016) Odporność na błędy użytkownika

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Niezawodność*                                                                                                                            |
| **Priorytet**          | *Średni*                                                                                                                                  |
| **Trudność**           | *Średnia*                                                                                                                               |
| **Sposób pomiaru**     | Testy manualne oraz analiza zgłoszeń błędów podczas sesji testowych.                                                                      |
| **Oczekiwane wartość** | ≤ 2 błędy krytyczne na 100 operacji.                                                                                                       |

---

#### (J0017) Definicja ról i uprawnień

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Bezpieczeństwo*                                                                                                                          |
| **Priorytet**          | *Kluczowy*                                                                                                                                |
| **Trudność**           | *Średnia*                                                                                                                               |
| **Sposób pomiaru**     | Audyt bezpieczeństwa oraz testy penetracyjne skoncentrowane na kontroli dostępu, weryfikacja polityki ról przy użyciu narzędzi audytowych.  |
| **Oczekiwane wartość** | 100% zgodność z założeniami polityki dostępu; brak możliwości nieautoryzowanego dostępu.                                                    |

---

#### (J0018) Odporność na cyberataki

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Bezpieczeństwo*                                                                                                                          |
| **Priorytet**          | *Kluczowy*                                                                                                                                |
| **Trudność**           | *Wysoka*                                                                                                                                  |
| **Sposób pomiaru**     | Audyt ekspercki oraz testy penetracyjne.                                                                                                  |
| **Oczekiwane wartość** | Brak zagrożeń krytycznych lub wysokich.                                                                                                   |

---

#### (J0019) Prowadzenie dziennika zdarzeń

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Bezpieczeństwo*                                                                                                                          |
| **Priorytet**          | *Kluczowy*                                                                                                                                |
| **Trudność**           | *Średnia*                                                                                                                               |
| **Sposób pomiaru**     | Testy audytowe – symulacja operacji, a następnie próba modyfikacji dziennika przy użyciu sum kontrolnych i mechanizmów zabezpieczających.    |
| **Oczekiwane wartość** | Każda operacja jest niezmiennie zapisywana; wszelkie próby modyfikacji kończą się niepowodzeniem.                                          |

---

#### (J0020) Zgodność z wymaganiami RODO

|                        |                                                                                                                                                   |
| ---------------------: | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Bezpieczeństwo*                                                                                                                                 |
| **Priorytet**          | *Kluczowy*                                                                                                                                       |
| **Trudność**           | *Wysoka*                                                                                                                                         |
| **Sposób pomiaru**     | Audyt ekspercki pod kątem zgodności prawnej i technicznej.                                                                                          |
| **Oczekiwane wartość** | 100% spełnienie wymagań RODO, brak niezgodności.                                                                                                  |

---

#### (J0021) Modularność i reużywalność komponentów

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Łatwość utrzymania*                                                                                                                      |
| **Priorytet**          | *Średni*                                                                                                                                  |
| **Trudność**           | *Średnia*                                                                                                                               |
| **Sposób pomiaru**     | Audyt architektury systemu przeprowadzony przez niezależnych ekspertów, oceniający możliwość modyfikacji pojedynczych modułów bez wpływu na całość. |
| **Oczekiwane wartość** | Ocena ekspercka ≥ 90% zgodności z wymaganiami modułowości; modyfikacja jednego modułu nie wpływa na działanie innych.                         |

---

#### (J0022) Testowalność krytycznych funkcji

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Łatwość utrzymania*                                                                                                                      |
| **Priorytet**          | *Średni*                                                                                                                                  |
| **Trudność**           | *Średnia*                                                                                                                               |
| **Sposób pomiaru**     | Wykorzystanie narzędzi do analizy pokrycia kodu (np. SonarQube) oraz pomiar czasu wykonania pełnego zestawu testów automatycznych.          |
| **Oczekiwane wartość** | Pokrycie krytycznych funkcji = 100%; czas wykonania testów ≤ 5 minut.                                                                       |

---

#### (J0023) Uruchomienie systemu na różnych systemach operacyjnych

|                        |                                                                                                                                           |
| ---------------------: | :---------------------------------------------------------------------------------------------------------------------------------------- |
| **Typ**                | *Przenośność*                                                                                                                             |
| **Priorytet**          | *Średni*                                                                                                                                  |
| **Trudność**           | *Średnia*                                                                                                                               |
| **Sposób pomiaru**     | Testy instalacyjne przeprowadzone na systemach macOS, Windows oraz Linux przy użyciu automatycznych skryptów instalacyjnych oraz manualna weryfikacja funkcjonalności. |
| **Oczekiwane wartość** | System uruchamia się bez modyfikacji kodu źródłowego na wszystkich trzech platformach; funkcjonalność identyczna (zgodność 100%).          |
