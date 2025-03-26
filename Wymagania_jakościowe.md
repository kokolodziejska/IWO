# Wymagania jakościowe
Wymagania jakościowe (pozafunkcjonalne) — weryfikujemy poprzez sprawdzenie jak system robi to, co ma robić.

Nazwy wymagań jakościowych najczęściej formułuje się w postaci prostych zdań zawierających orzeczenia modalne oparte na czasownikach takich jak „musieć”, „być”, „zawierać”.
(Np. System powinien wyświetlać mapę terenu przeciętnie w 2 sekundy.)

## Efektywność wydajnościowa 
Obejmuje zbiór atrybutów opisujących powiązania między poziomem wydajności oprogramowania a wykorzystywanymi zasobami (konfiguracją sprzętu, oprogramowania, materiałami eksploatacyjnymi) przy spełnieniu określonych warunków.

- Czas (ang. time behaviour) – czas odpowiedzi i wskaźniki przepustowości systemu.
Np. System powinien minimalizować czas otwierania bramek wejściowo/wyjściowych, aby utrzymać płynny ruch osób.

- Zużycie zasobów (ang. resource utilization) – wykorzystanie zasobów technologicznych przez system.
Np. System będzie obciążał zasoby obliczeniowe maszyn wykonawczych w maksymalnie 50%.

- Pojemność (ang. capacity) – limity parametrów systemu, np. liczba użytkowników lub przechowywanych danych.
Np. System będzie zapewniał przechowywanie co najmniej 5 mln rekordów transakcji finansowych z możliwością zwiększania do 10 mln po 5 latach.

### Kornelia Kołodziejska


## Kompatybilność
Dotyczy zdolności systemu do współdziałania z innymi produktami, systemami i komponentami.

-	Współistnienie (ang. co-existence) – efektywne działanie systemu we współdzielonym środowisku.
Np. System musi zachowywać zadane poziomy wydajności w sytuacji, gdy w tym samym środowisku wykonawczym działa inny system.

- Interoperacyjność (ang. interoperability) – wymiana i wykorzystanie danych między systemami.
Np. System powinien mieć możliwość odczytywania danych z systemu magazynowego.
Np. System powinien udostępniać API umożliwiające odczyt i modyfikację parametrów przez aplikacje zewnętrzne.

### Michał	Bibrzycki
System musi zapewniać możliwość łatwej integracji z systemami zewnętrznymi, szczególnie z systemem CKAN, umożliwiając wymianę danych oraz ich metadanych.

## Użyteczność
Dotyczy dostosowania sposobu użycia systemu do potrzeb użytkowników.

- Rozpoznawalność odpowiedniości (ang. appropriateness recognizability)
Np. System będzie zapewniał możliwość zautomatyzowanego przejścia przez proces konfiguracji funkcji analizy.

- Łatwość nauczenia (ang. learnability)
Np. System musi zapewniać możliwość osiągnięcia odpowiedniej wydajności po trzygodzinnym przeszkoleniu.

- Operatywność (ang. operability)
Np. System musi zapewniać dostęp do funkcji analizatora skupień bezpośrednio z panelu głównego.
Np. Rejestracja nowego towaru przez przeszkolonego pracownika ma być szybsza o 20% niż w starym systemie.

- Zabezpieczenie przed błędami użytkownika (ang. user error protection)
Np. System musi zapobiegać wprowadzeniu błędnych parametrów spoza dozwolonego zakresu.

- Estetyka interfejsu użytkownika (ang. user interface aesthetics)
Np. System musi zapewniać zgodność kolorystyki interfejsu z księgą identyfikacji wizualnej firmy.

- Przystępność (ang. accessibility)
Np. System musi umożliwiać dostosowanie rozmiaru czcionek do użytkowników ze słabym wzrokiem (np. stopień C–).

### Bartek	Janota

## Rozpoznawalność odpowiedniości
- System powinien zapewniać kontekstowe podpowiedzi i wskazówki dla każdej głównej funkcjonalności, tak aby użytkownik natychmiast rozpoznawał, czy dana opcja jest adekwatna do realizowanego zadania.

## Łatwość uczenia
- System powinien udostępniać krótki, interaktywny przewodnik przy pierwszym uruchomieniu nowych funkcji, aby skrócić czas potrzebny na opanowanie podstaw.

### Mikołaj 	Tradecki (Operatywność / Zabezpieczenie przed błędami użytkownika)
System powinien charakteryzować się wysoką operatywnością, zapewniając użytkownikom możliwość efektywnego i szybkiego wykonywania kluczowych zadań związanych z przeglądaniem zbiorów danych, przy minimalnym wysiłku i liczbie interakcji

### Mikołaj 	Frączek (Estetyka interfejsu użytkownika / Przystępność)

## Niezawodność
Dotyczy utrzymania określonego poziomu działania systemu w danym czasie.

- Dojrzałość (ang. maturity)
Np. System powinien zapewniać wystąpienie co najwyżej jednego błędu klasy 1 w miesiącu.

- Dostępność (ang. availability)
Np. System będzie dostępny 24/7 z dopuszczalnymi przerwami do 4 godzin miesięcznie w nocy.
Np. System będzie posiadał aplikację offline zapewniającą dostęp do danych w przypadku braku Internetu.

- Odporność na błędy (ang. fault tolerance)
Np. System będzie działał prawidłowo mimo unieruchomienia połowy maszyn wykonawczych.

- Odtwarzalność (ang. recoverability)
Np. System musi zapewniać średni czas między awariami na poziomie 1 awarii klasy 1 na rok.
Np. System musi przywrócić dane po awarii klasy 2 w czasie 1 godziny z utratą danych mniejszą niż 2 minuty.

### Dominika	Kalinowska ( Dojrzałość / Dostępność)
### Mateusz	Borka (Odporność na błędy / Odtwarzalność)

## Bezpieczeństwo
Dotyczy ochrony danych i kontroli dostępu do systemu.

- Poufność (ang. confidentiality)
Np. Tylko osoby z poziomem autoryzacji 10 mają dostęp do parametrów analizatora.

- Integralność (ang. integrity)
Np. System powinien uniemożliwiać zmianę kodu sterującego bez odpowiednich uprawnień.

- Niezaprzeczalność (ang. non-repudiation)
Np. Wszystkie akcje muszą być rejestrowane wraz z identyfikatorem operatora.

- Odpowiedzialność (ang. accountability)
Np. System musi dodawać identyfikator użytkownika do każdej transakcji sprzedaży.

- Autentyczność (ang. authenticity)
Np. Każdy dokument musi być podpisywany podpisem elektronicznym zgodnym ze standardem Beta Plus.

### Jakub	Klenkiewicz (Poufność / Integralność )
- System powinien umożliwiać definiowanie ról i uprawnień, aby dostęp do poufnych danych mieli wyłącznie autoryzowani użytkownicy.


### Michał	Ciechan (Niezaprzeczalność / Odpowiedzialność ) 
System musi prowadzić szczegółowy dziennik zdarzeń, zawierający datę, czas, użytkownika oraz opis wykonanej akcji, który nie może zostać usunięty ani zmodyfikowany bez śladu.

### Maciej 	Ruakt ( Autentyczność)

## Łatwość utrzymania
Dotyczy nakładów pracy podczas modyfikacji i rozwoju systemu.

- Modularność (ang. modularity)
Np. Analizator plazmy będzie niezależnym komponentem używanym przez inne moduły.

- Reużywalność (ang. reusability)
Np. Komponent będzie mógł być stosowany w innych systemach bez modyfikacji.

- Łatwość analizy (ang. analysability)
Np. Kod będzie zawierał dokumentację zgodną ze standardem XYZ ułatwiającym identyfikację błędów.

- Łatwość zmiany (ang. modifiability)
Np. Projekt będzie zgodny z metodyką ABC, wspierającą łatwą modyfikację i komponentyzację.

- Testowalność (ang. testability)
Np. System będzie zawierał interfejs wspierający automatyzację testów narzędziem XYZ.

### Łukasz	Gumienniczuk ( Modularność / Reużywalność)

System musi umożliwiać niezależne wdrażanie i aktualizowanie poszczególnych modułów bez wpływu na działanie innych komponentów oraz zawierać moduły, które mogą być wielokrotnie wykorzystywane zarówno w różnych częściach aplikacji, jak i w innych systemach, bez konieczności ich modyfikacji.

### Michał	Jagodziński (Łatwość analizy / Łatwość zmiany / Testowalność)

System powinien zawierać zestaw testów jednostkowych i integracyjnych, które pokrywają co najmniej 90% funkcjonalności krytycznych, a ich uruchomienie nie powinno przekraczać 5 minut.

## Przenośność
Dotyczy możliwości działania systemu w różnych środowiskach.

- Adaptowalność (ang. adaptability)
Np. System będzie automatycznie dostosowywał układ menu do rozmiaru ekranu.

- Łatwość instalowania (ang. installability)
Np. System będzie instalowany automatycznie przez App Shop.

- Łatwość zamiany (ang. replaceability)
Np. Nowy system będzie realizował wszystkie funkcje systemu XYZ w wersji 3.4.
 
### Daria	Koval
System musi być zdolny do uruchomienia w środowisku macOS, Windows oraz Linux bez konieczności modyfikacji kodu źródłowego.
