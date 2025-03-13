# Dokumentacja

## Opis biznesu

### Wstawianie danych do systemu

#### Opis

1. Zgłoszenie zapotrzebowania na otwarcie danych

- Rola: Zgłaszający
- Opis: Zgłaszający zgłasza zapotrzebowanie na udostępnienie danych.
- Kolor: `#palegreen`

2. Analiza możliwości udostępnienia

- Rola: Administrator
- Opis: Administrator w oparciu o wcześniej zdefiniowane kryteria decyduje o tym czy dane tego typu można udostępnić. Jeżeli nie to proces się kończy.
- Kolor `#lightblue`

3. Weryfikacja istnienia danych

- Rola: Administrator
- Opis: Administrator sprawdza czy istnieje źródło, które udostępnia takie dane.
- Kolor: `#lightblue`
  3a. Tworzenie danych
- Rola: Administrator
- Opis: Administrator zaleca zebranie odpowiednich danych.
- Kolor: `#lightblue`

4. Zdefiniowanie metadanych

- Rola: Redaktor
- Opis: Redaktor definiuje zestaw metadanych opisujących dodawany zbiór.
- Kolor: `#gold`

5. Przygotowanie danych

- Rola: Redaktor
- Opis: Redaktor przygotowuje dane do udostępnienia, to może obejmować np. ich odpowiednie zformatowanie lub przeredagowanie.
- Kolor: `#gold`

6. Udostępnienie danych

- Rola: Redaktor
- Opis: Redaktor udostępnia dane w serwisie.
- Kolor: `#gold`1. Zgłoszenie

#### Diagram

```puml
@startuml
|#palegreen|Z| Zgłaszający
start
:Zgłoszenie zapotrzebowania na otwarcie danych;

|#lightblue|A| Administrator
:Analiza możliwości udostępnienia;
if (Czy można udostępnić?) then (Tak)
  :Weryfikacja istnienia danych;
  if (Dane istnieją?) then (Tak)
    :Przechodzimy dalej;
  else (Nie)
    :Tworzenie danych;
  endif

  |#gold|R| Redaktor
  :Zdefiniowanie metadanych;
  :Przygotowanie danych;
  :Udostępnienie danych;
  stop
|#lightblue|A| Administrator
else (Nie)
  :Brak możliwości udostępnienia;
  stop
endif
@enduml
```

### Przeglądanie danych

#### Opis

1. Rozpoczęcie przeglądania (wyszukiwanie)

- Rola: Użytkownik
- Opis: Użytkownik wybiera zbiór danych poprzez wyszukanie go lub z zewnętrznego linku.
- Kolor: `#palegreen`

2. Sprawdzenie dostępności danych

- Rola: System
- Opis: System sprawdza dostępność danych. Jeżeli danych nieodnaleziono następuje koniec procesu.
- Kolor: `#lightblue`

3. Wyświetlenie danych

- Rola: Użytkownik
- Opis: Jeżeli wizualizacja jest możliwa, system wyświetla dane użytkownikowi w postaci np. diagramu bądź tabelki:
- Kolor: `#palegreen`

3. Pobranie danych

- Rola: Użytkownik
- Opis: Jeżeli wizualizacja nie jest dostępna użytkownik pobiera dane np. w postaci plików csv.
- Kolor: #palegreen

#### Diagram

```puml
@startuml

|#palegreen|U| Użytkownik
start
:Rozpoczęcie przeglądania (wyszukiwanie);

|#lightblue|S| System
:Sprawdzenie dostępności danych;
if (Czy dane odnaleziono?) then (Nie)
  :Brak danych;
  stop
else (Tak)
  if (Czy możliwa wizualizacja?) then (Tak)
    |U|
    :Wyświetlanie danych;
    stop
  else (Nie)
    |U|
    :Pobranie danych;
    stop
  endif
endif

@enduml
```

### Zgłaszanie uwag

#### Opis

1. Otworzenie zbioru danych

- Rola: Użytkownik
- Opis: Użytkownik otwiera zbiór danych
- Kolor: `#palegreen`

2. Zgłoszenie uwagi

- Rola: Użytkownik
- Opis: Użytkownik zgłasza uwagę
- Kolor: `#palegreen`

3. Obsłużenie uwagi

- Rola: Redaktor
- Opis: Redaktor decyduje, czy zgłoszenie tyczy się zbioru danych i czy ma jakiś wpływ na zgloszone obiekcje.
- Kolor: `#lightblue`

3. Zaakceptowanie uwagi
   - Rola: Redaktor
   - Opis: Redaktor zgłasza problem do administracji.
   - Kolor: `#lightblue`
4. Odrzucenie uwagi
   - Rola: Redaktor
   - Opis: Redaktor odrzuca uwagę i nie podejmuje dalszych kroków.
   - Kolor: #lightblue

#### Diagram

```puml
@startuml

|#palegreen|U| Użytkownik
start
:Wyszukanie zbioru danych;
:Wyświetlenie zbioru danych;
:Zgłoszenie uwagi;

|#lightblue|R| Redaktor
:Obsłużenie uwagi;
if (Uwaga zostaje zaakceptowana?) then (Tak)
  :Zaakceptowanie uwagi;
else (Nie)
  :Odrzucenie uwagi;
endif
stop
@enduml
```

### Zarządzanie schematami danych

#### Opis

1. Wyszukanie zbioru danych
   - Rola: Redaktor
   - Opis: Wyszukanie zbioru danych w celu zarządzania jego schematem danych.
   - Kolor: #palegreen
2. Zdefiniowanie schematu
   - Rola: Redaktor
   - Opis: Definiowanie struktury danych, włączając typy danych, ograniczenia i relacje pomiędzy elementami danych.
   - Kolor: #palegreen
3. Weryfikacja schematu
   - Rola: System
   - Opis: Automatyczna walidacja zbiorów danych względem przypisanych schematów w celu identyfikacji rozbieżności i błędów.
   - Kolor: #lightblue
   1. Poprawa schematu
      - Rola: Redaktor
      - Opis: Redaktor identyfikuje dane, które nie są zgodne ze schematem i wprowadza odpowiednie modyfikacje.
      - Kolor: #lightblue
4. Publikacja schematu
   - Rola: Redaktor
   - Opis: Udostępnianie schematów użytkownikom i systemom, które potrzebują zrozumieć strukturę zbiorów danych.
   - Kolor: #palegreen

#### Diagram

```puml
@startuml

|#palegreen|R| Redaktor
start
:Wyszukanie zbioru danych;
:Zdefiniowanie schematu;

|#lightblue|S| System
:Weryfikacja schematu;
if (Dane są zgodne ze schematem) then (Tak)
else (Nie)
    |R|
    :Poprawa schematu;
endif
|R|
:Publikacja schematu;
stop
@enduml
```

### Subskrybcja do powiadomień o zmianie danych

#### Opis

1. Wyszukanie zbioru danych
   - Rola: Użytkownik
   - Opis: Użytkownik wyszukuje zbioru danych w celu zasubskrybowania do powiadomień o zmianie danych.
   - Kolor: #palegreen
2. Subskrybcja do zbioru danych
   - Rola: Użytkownik
   - Opis: Użytkownik zapisuje się na powiadomienia dotyczące wybranego zbioru danych, aby otrzymywać informacje o jego aktualizacjach.
   - Kolor: #palegreen
3. Wysłanie powiadomienia o zmianie danych.
   - Rola: System
   - Opis: System automatycznie wysyła powiadomienie do subskrybentów w momencie wykrycia zmiany w subskrybowanym zbiorze danych.
   - Kolor: #lightblue

#### Diagram

```puml
@startuml
|#palegreen|U| Użytkownik
start
:Wyszukanie zbioru danych;
:Subskrybcja do zbioru danych;

|#lightblue|S| System
while (Dane się zmieniły?) is (Tak)
    :Wysłanie powiadomienia o zmianie danych;
endwhile

-[hidden]->
detach
@enduml
```

### Konwersja formatu danych

#### Opis

1. Wyszukanie zbioru danych
   - Rola: Użytkownik
   - Opis: Użytkownik wyszukuje zbioru danych w celu pobrania danych.
   - Kolor: #palegreen
2. Zgłoszenie chęci pobrania danych w innym formacie niż dostępne.
   - Rola: Użytkownik
   - Opis: Użytkownik chce pobrać dane w przekonwertowanym formacie.
   - Kolor: #palegreen
3. Analiza schematu danych

   - Rola: System
   - Opis: System sprawdza strukturę i zgodność zbioru danych, żeby umożliwić ewentualną konwersję.
   - Kolor: #lightblue

   1. Zgłoszenie uwagi

      - Rola: Użytkownik
      - Opis: Użytkownik zgłasza uwagi dotyczące danych, np. brak schematu.
      - Kolor: #palegreen

   1. Konwersja danych do odpowiedniego formatu
      - Rola: System
      - Opis: System automatycznie przekształca dane do formatu wskazanego przez użytkownika, jeśli konwersja jest możliwa.
      - Kolor: #lightblue
   1. Pobranie danych
      - Rola: Użytkownik
      - Opis: Użytkownik pobiera dane w wybranym formacie.
      - Kolor: #palegreen

#### Diagram

```puml
@startuml
|#palegreen|U| Użytkownik
start
:Wyszukanie zbioru danych;
:Zgłoszenie chęci pobrania danych w innym formacie niż dostępne;

|#lightblue|S| System
:Analiza schematu danych;
if (Czy dane mają przypisany schemat?) then (Tak)
    :Konwersja danych do odpowiedniego formatu;

    |U|
    :Pobranie danych;
else (Nie)
    |U|
    :Zgłoszenie uwagi;
endif
stop
@enduml
```

## Wizja systemu

### 1. Abstrakt

Niniejszy dokument przedstawia wizję systemu zarządzania otwartymi danymi publicznymi, który odpowiada na istotny problem utrudnionego dostępu, przetwarzania i udostępniania informacji publicznej. Projektowany system zapewni efektywne zarządzanie oraz dynamiczne publikowanie danych pochodzących od administracji publicznej, co przyczyni się do poprawy ich jakości, aktualności oraz przejrzystości. W dokumencie wyszczególniono wymagania funkcjonalne oraz jakościowe systemu, uwzględniające kluczowe potrzeby wszystkich zidentyfikowanych interesariuszy. Zaproponowano również motto projektu: **„Otwarte dane – otwarte możliwości”** które ma skutecznie wspierać kampanie promocyjne, budować świadomość społeczną oraz wzmacniać poczucie zaangażowania zespołu projektowego.

### 2. Problem

#### 2.1 Istota problemu

Główny problem klienta polega na braku efektywnego systemu do zarządzania otwartymi danymi publicznymi, co utrudnia dostęp do informacji, ich przetwarzanie i udostępnianie. Powiązany jest z nim szereg innych, opisanych poniżej problemów.

#### 2.2 Specyfikacja problemów

- **(P0001) Brak efektywnego systemu do zarządzania otwartymi danymi publicznymi**

  **Priorytet: Kluczowy** | **Trudność: Średnia**

  **Opis:** Problem polega na braku spójnego, efektywnego systemu do zarządzania i udostępniania otwartych danych publicznych, który dotyczy przede wszystkim administracji publicznej, ale również obywateli, przedsiębiorców, analityków, organizacji pozarządowych oraz mediów. Rezultatem problemu są utrudnienia w dostępie do aktualnych, rzetelnych oraz kompletnych informacji publicznych, niska przejrzystość działań administracji oraz ograniczone możliwości efektywnego wykorzystania tych danych do tworzenia analiz, raportów czy rozwiązań innowacyjnych. Problem można rozwiązać poprzez stworzenie nowoczesnego systemu zarządzania otwartymi danymi publicznymi, który zapewni skuteczne zarządzanie, dynamiczne udostępnianie oraz intuicyjny dostęp do danych wraz z narzędziami analitycznymi i wizualizacyjnymi. Rozwiązanie tego problemu umożliwi łatwiejsze podejmowanie decyzji opartych o dane, zwiększy przejrzystość administracji publicznej, przyczyni się do wzrostu zaangażowania obywatelskiego oraz poprawi warunki do rozwoju społeczno-gospodarczego.

- **(P0002) Problem niedostatecznego wykorzystania danych publicznych**

  **Priorytet:** Wyoski | **Trudność:** Średnia

  **Opis:** Problem polega na niedostatecznym wykorzystaniu udostępnianych danych publicznych przez obywateli i przedsiębiorców, co podważa sensowność ponoszenia kosztów związanych z ich publikacją i utrzymaniem. Problem dotyczy administracji publicznej, obywateli oraz przedsiębiorców. Rezultatem jest niewystarczająca transparentność oraz niski zwrot z inwestycji w udostępnianie danych. Problem można rozwiązać, budując system oferujący dane w przystępnej formie, umożliwiający ich łatwą analizę, wizualizację oraz integrację. Korzyścią będzie zwiększenie zainteresowania danymi, większa transparentność działań administracji publicznej oraz tworzenie nowych innowacyjnych rozwiązań.

- **(P0003) Problem niskiej aktualności i wiarygodności danych**

  **Priorytet:** Kluczowy | **Trudność:** Średnia

  **Opis:** Problem dotyczy niskiej aktualności oraz wiarygodności udostępnianych danych publicznych, co ogranicza ich praktyczne zastosowanie. Problem ten dotyczy użytkowników danych (obywateli, przedsiębiorców, analityków). Jego rozwiązaniem jest budowa systemu z mechanizmami automatycznej aktualizacji, walidacji danych i śledzenia ich pochodzenia. Korzyścią będzie wzrost jakości i wiarygodności danych, a także ułatwienie podejmowania trafnych decyzji na podstawie tych danych.

- **(P0004) Problem integracji danych z innymi systemami**

  **Priorytet:** Kluczowy | **Trudność:** Wysoka

  **Opis:** Problem polega na trudnościach z integracją danych z zewnętrznymi systemami i aplikacjami, co ogranicza możliwości ponownego wykorzystania danych oraz innowacji. Dotyczy programistów, przedsiębiorców oraz analityków danych. Rozwiązaniem problemu jest wdrożenie jasnych standardów wymiany danych (np. CKAN, DCAT, RDF) oraz zapewnienie API umożliwiającego łatwą integrację. Korzyści wynikające z rozwiązania to zwiększenie interoperacyjności systemów, redukcja kosztów integracji oraz zwiększenie liczby aplikacji korzystających z danych publicznych.

- **(P0005) Brak narzędzi do analizy danych przez nietechnicznych użytkowników**

  **Priorytet:** Średni | **Trudność:** Średnia

  **Opis:** Problem dotyczy braku łatwych w użyciu narzędzi analitycznych, które pozwoliłyby użytkownikom bez specjalistycznej wiedzy technicznej samodzielnie eksplorować dane. Dotyka głównie obywateli, dziennikarzy, aktywistów i organizacje pozarządowe. Rozwiązaniem jest dostarczenie intuicyjnych narzędzi wizualizacyjnych (mapy, wykresy, raporty). Korzyści to zwiększenie samodzielności użytkowników, lepsze zrozumienie danych oraz ich szersze wykorzystanie społeczne.

- **(P0006) Brak jednolitej polityki otwierania danych publicznych**

  **Priorytet:** Wysoki | **Trudność:** Wysoka

  **Opis:** Problemem jest brak jednolitej polityki otwierania danych w administracji publicznej, co powoduje niejednolitość danych, ich słabą jakość oraz ograniczoną dostępność. Dotyczy to administracji publicznej, analityków, programistów oraz obywateli. Rozwiązaniem będzie wdrożenie spójnej polityki publikowania danych publicznych opartej na standardach jakości (DCAT, CKAN, RDF). Korzyścią jest zwiększenie dostępności i jakości danych, poprawa transparentności oraz wsparcie innowacyjności i rozwoju społeczno-gospodarczego.

- **(P0007) Niska świadomość społeczna na temat dostępnych danych**

  **Priorytet:** Średni | **Trudność:** Średnia

  **Opis:** Problem polega na niewystarczającej świadomości społecznej na temat korzyści płynących z otwartych danych publicznych. Dotyczy głównie obywateli i lokalnych społeczności. Rozwiązaniem jest kampania promocyjna oraz edukacyjna wprowadzona równolegle z systemem. Korzyści to wzrost świadomości społecznej, większe zainteresowanie danymi oraz poprawa jakości życia obywateli dzięki lepszemu wykorzystaniu dostępnych informacji publicznych.

- **(P0008) Trudność w zarządzaniu dużą ilością metadanych**

  **Priorytet:** Wysoki | **Trudność:** Średnia

  **Opis:** Problemem jest trudność zarządzania dużą ilością różnorodnych metadanych, co prowadzi do błędów, utrudnia wyszukiwanie danych i obniża jakość informacji. Rozwiązaniem jest wdrożenie intuicyjnych narzędzi do efektywnego zarządzania metadanymi zgodnymi ze standardem DCAT/AP. Korzyścią będzie usprawnienie zarządzania danymi, poprawa jakości ich dostępności oraz zwiększenie efektywności analizy informacji.

### 3. Motto

Motto projektu jest kluczowym elementem komunikacji, które wspiera kampanie promocyjne systemu, buduje świadomość społeczną oraz łatwo zapada w pamięć. Dodatkowo powinno inspirować, motywować oraz wzmacniać morale zespołu projektowego, budując ich poczucie przynależności i zaangażowanie we wspólne cele.

Proponujemy motto główne projektu

### Otwarte dane - otwarte możliwości

Pozostałe pomysły brane pod uwagę przy wyborze motto:

- „Otwarte dane. Wiedza, która zmienia świat.”

- „Otwórz dane, otwórz przyszłość.”

- „Otwarte dane – Twoje prawo do wiedzy.”

- „Dane publiczne – siła w transparentności.”

- „Dostęp do wiedzy kluczem do rozwoju.”

- „Otwórz się na dane, a dane otworzą się na Ciebie.”

- „Dane otwarte zmieniają rzeczywistość.”

### 4. Interesariusze

Tworzony system zarządzania publicznymi danymi otwartymi musi odpowiadać na potrzeby różnych grup interesariuszy. Poniżej przedstawiono szczegółową charakterystykę interesariuszy oraz określono kluczowe interesy każdej z grup.

#### 4.1 Administrator systemu

_Osoba lub grupa osób odpowiedzialna za bieżące zarządzanie, konfigurowanie i monitorowanie systemu._

**Kluczowe interesy:**

- Sprawne i wygodne zarządzanie systemem oraz zgromadzonymi zasobami danych.

- Intuicyjne narzędzia administracyjne umożliwiające efektywną kontrolę dostępu oraz zarządzanie użytkownikami.

- Łatwość monitorowania stanu systemu, diagnostyka problemów oraz szybkie reagowanie na awarie.

#### 4.2 Użytkownicy końcowi

_Osoby, które będą bezpośrednio korzystać z danych dostępnych w systemie (obywatele, badacze, studenci, dziennikarze, aktywiści społeczni, analitycy danych, firmy komercyjne)._

**Kluczowe interesy:**

- Łatwy i szybki dostęp do aktualnych, rzetelnych oraz wiarygodnych danych publicznych.

- Intuicyjny i responsywny interfejs umożliwiający efektywne wyszukiwanie, filtrowanie oraz wizualizację danych.

- Możliwość eksportu danych do wybranego formatu.

- Możliwość korzystania z danych anonimowo, bez konieczności logowania.

- Możliwość subskrypcji i otrzymywania powiadomień o aktualizacjach interesujących danych.

#### 4.3 Klienci organizacji

_Podmioty gospodarcze lub osoby fizyczne, które współpracują lub korzystają z usług organizacji dostarczającej dane._

**Kluczowe interesy:**

- Dostęp do otwartych danych umożliwiających realizację celów biznesowych, naukowych, edukacyjnych lub społecznych.

- Możliwość integracji danych publicznych ze swoimi własnymi systemami informatycznymi poprzez wygodne API.

- Gwarancja wysokiej jakości oraz aktualności udostępnianych danych.

#### 4.4 Inwestorzy i sponsorzy

_Podmioty finansujące projekt oraz oczekujące pozytywnego wpływu inwestycji na społeczeństwo lub gospodarkę lokalną._

**Kluczowe interesy:**

- Efektywne wykorzystanie środków publicznych przeznaczonych na realizację projektu.

- Transparentność projektu, wysoka jakość danych oraz zgodność systemu ze standardami krajowymi i międzynarodowymi.

- Poprawa wizerunku oraz zwiększenie zaufania obywateli wobec instytucji publicznych.

#### 4.5 Zamawiający

_Osoby podejmujące decyzje strategiczne związane z wdrożeniem systemu._

**Kluczowe interesy:**

- Wdrożenie systemu, który rozwiązuje kluczowe problemy administracji publicznej oraz wpisuje się w długoterminowe cele strategiczne jednostki.

- Możliwość łatwej weryfikacji efektywności systemu oraz jakości udostępnianych danych.

- Realizacja celów politycznych, społecznych oraz strategicznych poprzez wdrożenie skutecznego systemu danych otwartych.

#### 4.6 Dział IT

_Osoby odpowiedzialne za utrzymanie, rozwój techniczny oraz administrację infrastruktury informatycznej obsługującej system._

**Kluczowe interesy:**

- System stabilny, niezawodny i łatwy w utrzymaniu.

- Wykorzystanie nowoczesnych, bezpiecznych, dobrze udokumentowanych i aktywnie wspieranych technologii.

- Łatwa diagnostyka, monitoring oraz automatyzacja procesów związanych z zarządzaniem systemem.

- Zapewnienie skalowalności, bezpieczeństwa oraz ciągłej aktualizacji systemu.

#### 4.7 Partnerzy i integratorzy danych

_Zewnętrzne organizacje i instytucje dostarczające dane lub współpracujące z systemem na zasadzie integracji lub wymiany danych._

**Kluczowe interesy:**

- Wygodne mechanizmy integracji oraz automatyzacji transferu danych pomiędzy różnymi systemami.

- Jasno określone standardy wymiany danych (np. DCAT, CKAN, RDF).

- Szybka walidacja oraz możliwość błyskawicznego publikowania aktualizacji danych po stronie platformy.

#### 4.8 Analitycy i eksperci ds. danych

_Osoby zajmujące się analizą danych oraz ich wykorzystaniem do tworzenia raportów, analiz lub prognoz (badacze, specjaliści ds. urbanistyki, transportu, jakości powietrza itp.)._

**Kluczowe interesy:**

- Możliwość zaawansowanego wyszukiwania, filtrowania oraz eksportowania dużych zbiorów danych.

- Dostęp do narzędzi umożliwiających analizę oraz wizualizację danych (w tym predykcje i analizy za pomocą rozwiązań AI).

- Łatwe cytowanie oraz generowanie poprawnych opisów bibliograficznych do publikacji naukowych.

#### 4.9 Społeczność lokalna (obywatele)

_Mieszkańcy oraz społeczność lokalna, którzy mają bezpośredni lub pośredni wpływ na wykorzystanie danych publicznych._

**Kluczowe interesy:**

- Przejrzystość działania administracji oraz dostęp do aktualnych informacji (np. transport publiczny, zanieczyszczenie powietrza).

- Możliwość zgłaszania opinii oraz uwag dotyczących jakości danych lub ich prezentacji.

- Uzyskanie wymiernych korzyści społecznych i poprawa jakości życia dzięki efektywnemu wykorzystaniu danych.

### 5. Cechy systemu

#### 5.1 Cechy funkcjonalne

- **(CF0001) Rejestracja i zarządzanie użytkownikami**

  **Priorytet:** Kluczowy | **Trudność**: Średnia

  **Opis**:  
  System musi umożliwiać rejestrację nowych użytkowników oraz zarządzanie ich kontami przez administratora.

- **(CF0002) Anonimowy dostęp do danych publicznych (bez logowania)**

  **Priorytet:** Kluczowy | **Trudność**: Niska

  **Opis**:  
  System musi zapewnić użytkownikom możliwość dostępu do publicznych zbiorów danych bez konieczności logowania.

- **(CF0003) Import i eksport danych zgodny ze schematami (CSV, XML, JSON)**

  **Priorytet:** Kluczowy | **Trudność**: Średnia

  **Opis**:  
  System musi umożliwiać importowanie oraz eksportowanie danych zgodnie ze zdefiniowanymi schematami, obsługując formaty CSV, XML oraz JSON.

- **(CF0004) Pobieranie danych z zewnętrznych źródeł/API**

  **Priorytet:** Kluczowy | **Trudność**: Średnia

  **Opis**:  
  System musi umożliwiać automatyczne pobieranie danych z zewnętrznych źródeł (pliki, urządzenia pomiarowe, API) oraz ich dalszą integrację.

- **(CF0005) Automatyczna walidacja danych zgodnie z DCAT/AP**

  **Priorytet:** Kluczowy | **Trudność**: Wysoka

  **Opis**:  
  System musi automatycznie walidować importowane dane według standardu DCAT/AP, zapewniając ich spójność oraz zgodność.

- **(CF0006) Zgodność z piątym poziomem otwartości danych (RDF)**

  **Priorytet:** Kluczowy | **Trudność**: Wysoka

  **Opis**:  
  System musi zapewniać dostępność danych na piątym poziomie otwartości według klasyfikacji 5-star (standard RDF).

- **(CF0007) Dynamiczne udostępnianie danych poprzez API**

  **Priorytet:** Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System musi umożliwiać dynamiczne, automatyczne udostępnianie zbiorów danych publicznych poprzez interfejs API.

- **(CF0008) Udostępnianie różnych dystrybucji tego samego zbioru danych**

  **Priorytet:** Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System musi umożliwiać udostępnianie tego samego zbioru danych w różnych dystrybucjach.

- **(CF0009) Wersjonowanie danych**

  **Priorytet:** Wysoki | **Trudność**: Średnia

  **Opis**:  
   System musi zapewniać mechanizm wersjonowania danych z możliwością dostępu do ich wcześniejszych wersji.

- **(CF0010) Obsługa schematów danych (przypisywanie, walidacja, zarządzanie)**

  **Priorytet:** Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi umożliwiać zarządzanie, przypisywanie oraz walidację schematów danych dla konkretnych zbiorów.

- **(CF0011) Zaawansowane wyszukiwanie i filtrowanie zbiorów danych po wielu zmiennych**

  **Priorytet:** Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System musi oferować zaawansowane mechanizmy wyszukiwania i filtrowania zbiorów danych według wielu różnych kryteriów.

- **(CF0012) Stronicowanie wyników wyszukiwania**

  **Priorytet:** Wysoki | **Trudność**: Niska

  **Opis**:  
   System musi umożliwiać stronicowanie wyników wyszukiwania, zapewniając przejrzystość prezentowanych danych.

- **(CF0013) Generowanie tabel z funkcją filtrowania i sortowania danych**

  **Priorytet:** Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System musi umożliwiać prezentację danych w postaci tabelarycznej z opcją filtrowania i sortowania.

- **(CF0014) Interaktywne wizualizacje danych**

  **Priorytet:** Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi oferować możliwość interaktywnej wizualizacji danych, m.in. w formie wykresów oraz map. Zbiory danych powinny być oznaczane w odpowiedni sposób, aby zostały zwizualizowane zgodnie z zapotrzebowaniem.

- **(CF0015) Łatwe cytowanie danych i generowanie bibliografii**

  **Priorytet:** Średni | **Trudność**: Średnia

  **Opis**:  
   System musi umożliwiać użytkownikom łatwe cytowanie danych oraz automatyczne generowanie opisów bibliograficznych zgodnych z przyjętymi standardami.

- **(CF0016) Zarządzanie metadanymi zbiorów (standard DCAT/AP)**

  **Priorytet:** Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System musi umożliwiać zarządzanie metadanymi zbiorów danych zgodnie ze standardem DCAT/AP.  
   Mechanizm ma obejmować stworzenie i konfigurację własnych zestawów metadanych oraz możliwość eksportu i importu zestawów metadanych.  
   Metadane danego zbioru powinny być edytowane zgodnie z jego przypisanym zestawem.

- **(CF0017) Zgłaszanie uwag do zbiorów danych przez użytkowników**

  **Priorytet:** Wysoki | **Trudność**: Średnia

  **Opis**:  
   System musi zapewnić użytkownikom możliwość zgłaszania uwag dotyczących jakości lub zawartości zbiorów danych.

- **(CF0018) Mechanizm zarządzania zgłoszeniami użytkowników**

  **Priorytet:** Wysoki | **Trudność**: Średnia

  **Opis**:  
   System musi posiadać mechanizm zarządzania zgłoszeniami od użytkowników, umożliwiający ich dalszą analizę i eskalację – wysyłkę konieczności wprowadzenia zmian przez dostawcę zbioru danych, obsługę odpowiedzi od dostawcy, zmianę statusu zgłoszenia, wysyłkę komunikatu o akceptacji bądź odrzuceniu zgłoszenia do zgłaszającego.

- **(CF0019) Powiadomienia o aktualizacjach subskrybowanych danych**

  **Priorytet:** Średni | **Trudność**: Średnia

  **Opis**:  
   System musi umożliwiać użytkownikom otrzymywanie powiadomień o aktualizacjach wybranych zbiorów danych za pomocą różnych kanałów komunikacji (e-mail, SMS, w aplikacji).

- **(CF0020) Indeksowanie danych i pozycjonowanie w przeglądarce**

  **Priorytet:** Wysoki | **Trudność**: Średnia

  **Opis**:  
   System musi umożliwiać indeksowanie zbiorów danych przez wyszukiwarki, zapewniając lepsze ich pozycjonowanie.

- **(CF0021) Dwuskładnikowa autoryzacja**

  **Priorytet:** Wysoki | **Trudność**: Średnia

  **Opis**:  
   System musi zapewniać możliwość dwuskładnikowego uwierzytelniania użytkowników przy pomocy standardu OAuth2.0.

#### 5.1.1 Pomysły na przyszłość

- **(CFP0001) Odpłatne udostępnianie wybranych danych w modelu subskrypcyjnym**

  **Priorytet:** Pomysł | **Trudność**: Średnia

  **Opis**:  
   System powinien umożliwić administratorowi odpłatne udostępnianie wybranych zbiorów danych na zasadach subskrypcji.

- **(CFP0002) Zmiana motywu graficznego wizualizacji przez użytkownika**

  **Priorytet:** Pomysł | **Trudność**: Niska

  **Opis**:  
   System powinien umożliwić użytkownikowi końcowemu samodzielną zmianę motywu graficznego wizualizacji danych według własnych preferencji.

- **(CFP0003) Predykcje dla odpowiednio oznaczonych zbiorów danych (z szeregiem czasowym)**

  **Priorytet:** Pomysł | **Trudność**: Wysoka

  **Opis**:  
   System powinien umożliwiać analitykom i użytkownikom generowanie predykcji na podstawie zbiorów danych posiadających szereg czasowy, wykorzystując modele prognostyczne.

- **(CFP0004) Statystyki użycia/pobrań danych**

  **Priorytet:** Pomysł | **Trudność**: Średnia

  **Opis**:  
   System powinien automatycznie gromadzić i prezentować statystyki dotyczące popularności i częstotliwości pobrań lub użycia danych przez użytkowników.

- **(CFP0005) Generowanie raportów użytecznych dla audytorów danych**

  **Priorytet:** Pomysł | **Trudność**: Średnia

  **Opis**:  
   System powinien umożliwić generowanie raportów zawierających informacje przydatne dla audytorów, takie jak historia zmian danych, ich źródło oraz jakość metadanych.

- **(CFP0006) Reklamy**

  **Priorytet:** Pomysł | **Trudność**: Niska

  **Opis**:  
   System powinien umożliwiać administratorowi zarządzanie i wyświetlanie reklam.

- **(CFP0007) Captcha**

  **Priorytet:** Pomysł | **Trudność**: Niska

  **Opis**:  
   System powinien oferować możliwość zabezpieczenia wybranych funkcjonalności (np. rejestracja, formularze kontaktowe) mechanizmem Captcha, chroniąc przed spamem i botami.

- **(CFP0008) Dostęp offline do wybranych danych**

  **Priorytet:** Pomysł | **Trudność**: Wysoka

  **Opis**:  
   System powinien umożliwiać użytkownikom dostęp do wybranych zbiorów danych w trybie offline, np. poprzez aplikację mobilną lub pobranie danych na urządzenie lokalne.

- **(CFP0009) Integracja z ChatGPT lub innymi rozwiązaniami AI**

  **Priorytet:** Pomysł | **Trudność**: Wysoka

  **Opis**:  
   System powinien wspierać integrację z modelami sztucznej inteligencji, takimi jak ChatGPT, umożliwiając użytkownikom prowadzenie interaktywnych analiz oraz generowanie wniosków na podstawie danych.

#### 5.2 Cechy jakościowe

- **(CJU0001) Intuicyjny i łatwy w obsłudze interfejs użytkownika**

  **Typ**: Użyteczność | **Priorytet**: Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System powinien posiadać intuicyjny interfejs użytkownika, zapewniający szybkie opanowanie obsługi i łatwe wykonywanie podstawowych operacji.

  **Metryka**:  
   Średni wynik w skali SUS (System Usability Scale) powyżej 70 punktów, uzyskany od reprezentatywnej grupy użytkowników.

  **Sposób pomiaru**:  
   Ankieta SUS przeprowadzona po zakończeniu sesji testowej z użytkownikami.

  **Możliwe wyniki pomiaru**:  
   Wynik w skali SUS (0-100).

  **Akceptowalne wartości pomiaru**:  
   Powyżej 70 punktów.

- **(CJU0002) Responsywny interfejs**

  **Typ**: Użyteczność | **Priorytet**: Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System powinien dostosowywać interfejs użytkownika do urządzeń mobilnych, tabletów i desktopów, zapewniając optymalny wygląd i obsługę.

  **Metryka**:  
   Czas ładowania interfejsu (mobile).

  **Sposób pomiaru**:  
   Testy responsywności (narzędzia Lighthouse, GTmetrix).

  **Możliwe wyniki pomiaru**:  
   W sekundach.

  **Akceptowalne wartości pomiaru**:  
   ≤3 sekundy w sieci 3G.

- **(CJU0003) Dostępność zgodna z WCAG 2.1 (AA)**

  **Typ**: Użyteczność | **Priorytet**: Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi spełniać standard WCAG 2.1 na poziomie AA, zapewniając dostępność dla osób z niepełnosprawnościami.

  **Metryka**:  
   Procent spełnionych kryteriów WCAG 2.1 AA.

  **Sposób pomiaru**:  
   Audyt dostępności (narzędzia automatyczne oraz audyt ekspercki).

  **Możliwe wyniki pomiaru**:  
   0–100%.

  **Akceptowalne wartości pomiaru**:  
   100% zgodności z poziomem AA.

- **(CJN0001) Dostępność systemu 24/7 (SLA 99,9%)**

  **Typ**: Niezawodność | **Priorytet**: Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi być dostępny całodobowo przez 7 dni w tygodniu, z gwarantowanym poziomem dostępności SLA wynoszącym minimum 99,9%.

  **Metryka**:  
   Procentowa dostępność systemu (uptime).

  **Sposób pomiaru**:  
   Narzędzia monitorujące (np. UptimeRobot).

  **Możliwe wyniki pomiaru**:  
   0–100%.

  **Akceptowalne wartości pomiaru**:  
   ≥99,9% miesięcznie.

- **(CJN0002) Regularne backupy i szybkie odtwarzanie danych**

  **Typ**: Niezawodność | **Priorytet**: Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System musi automatycznie tworzyć kopie zapasowe danych i umożliwiać szybkie odtworzenie danych po ewentualnej awarii.

  **Metryka**:  
   Czas odtworzenia danych (RTO) i częstotliwość backupów (RPO).

  **Sposób pomiaru**:  
   Testy przywracania danych.

  **Możliwe wyniki pomiaru**:  
   RTO: czas w godzinach; RPO: godziny pomiędzy kopiami.

  **Akceptowalne wartości pomiaru**:  
   RTO ≤2 godziny, RPO ≤24 godziny.

- **(CJB0001) Odporność na cyberataki**

  **Typ**: Bezpieczeństwo | **Priorytet**: Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi posiadać zabezpieczenia przed cyberatakami, zapewniając ochronę danych poprzez szyfrowanie, uwierzytelnianie oraz kontrolę dostępu.

  **Metryka**:  
   Wyniki audytu bezpieczeństwa.

  **Sposób pomiaru**:  
   Audyt ekspercki, testy penetracyjne.

  **Możliwe wyniki pomiaru**:  
   Liczba znalezionych zagrożeń.

  **Akceptowalne wartości pomiaru**:  
   Brak zagrożeń krytycznych/wysokich.

- **(CJW0001) Krótki czas odpowiedzi na zapytania**

  **Typ**: Efektywność wydajnościowa | **Priorytet**: Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi generować odpowiedzi na zapytania użytkowników (np. wyszukiwanie danych) w czasie krótszym niż 3 sekundy.

  **Metryka**:  
   Średni czas odpowiedzi serwera na zapytania użytkowników.

  **Sposób pomiaru**:  
   Automatyczne testy wydajnościowe, mierzone narzędziami do monitoringu serwera.

  **Możliwe wyniki pomiaru**:  
   Czas odpowiedzi (w sekundach).

  **Akceptowalne wartości pomiaru**:  
   Poniżej 3 sekund.

- **(CJW0002) Skalowalność systemu**

  **Typ**: Efektywność wydajnościowa | **Priorytet**: Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi efektywnie obsługiwać rosnącą liczbę użytkowników (do 100 000 jednoczesnych sesji) oraz dużą ilość danych (do 10 TB).

  **Metryka**:  
   Liczba równoczesnych użytkowników obsługiwanych przez system bez pogorszenia parametrów czasowych oraz ilość przetwarzanych danych.

  **Sposób pomiaru**:  
   Testy obciążeniowe symulujące do 100 000 jednoczesnych użytkowników oraz testy pojemności danych do 10 TB.

  **Możliwe wyniki pomiaru**:  
   Liczba jednoczesnych użytkowników, średni czas odpowiedzi systemu, wielkość obsługiwanych danych (TB).

  **Akceptowalne wartości pomiaru**:  
   Obsługa co najmniej 100 000 jednoczesnych użytkowników, czas odpowiedzi poniżej 3 sekund, obsługa co najmniej 10 TB danych.

- **(CJW0003) Wydajne przetwarzanie dużych zbiorów danych**

  **Typ**: Efektywność wydajnościowa | **Priorytet**: Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi szybko przetwarzać duże zbiory danych, np. importować 1 GB danych w czasie krótszym niż 15 minut.

  **Metryka**:  
   Czas importu dużych zbiorów danych (w minutach na GB).

  **Sposób pomiaru**:  
   Pomiar czasu importu dużych zbiorów danych przy użyciu automatycznych narzędzi.

  **Możliwe wyniki pomiaru**:  
   Czas potrzebny na przetworzenie/import 1 GB danych.

  **Akceptowalne wartości pomiaru**:  
   Mniej niż 15 minut na 1 GB danych.

- **(CJW0004) Minimalizacja zużycia zasobów serwera**

  **Typ**: Efektywność wydajnościowa | **Priorytet**: Niski | **Trudność**: Średnia

  **Opis**:  
   System powinien efektywnie wykorzystywać zasoby sprzętowe serwera, minimalizując zużycie procesora oraz pamięci RAM.

  **Metryka**:  
   Procentowe zużycie zasobów serwera (CPU, RAM) podczas typowego użytkowania systemu.

  **Sposób pomiaru**:  
   Monitoring serwera przy symulacji 50 000 jednoczesnych użytkowników za pomocą narzędzi diagnostycznych i monitorujących.

  **Możliwe wyniki pomiaru**:  
   Średnie obciążenie procesora (% CPU), średnie zużycie pamięci RAM (% RAM).

  **Akceptowalne wartości pomiaru**:  
   Zużycie CPU poniżej 50%, zużycie pamięci RAM poniżej 70%.

- **(CJM0001) Łatwa instalacja i konfiguracja**

  **Typ**: Łatwość utrzymania | **Priorytet**: Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System powinien być łatwy w instalacji oraz konfiguracji na różnych platformach, nie przekraczając 10 kroków konfiguracyjnych oraz 2 godzin instalacji.

  **Metryka**:  
   Liczba kroków instalacji oraz całkowity czas instalacji na nowym środowisku.

  **Sposób pomiaru**:  
   Pomiar czasu oraz liczby kroków konfiguracyjnych podczas testowej instalacji systemu na nowych środowiskach.

  **Możliwe wyniki pomiaru**:  
   Liczba kroków instalacji (całkowita), czas instalacji (w godzinach i minutach).

  **Akceptowalne wartości pomiaru**:  
   Maksymalnie 10 kroków konfiguracyjnych, czas instalacji krótszy niż 2 godziny.

- **(CJM0002) Diagnostyka i monitoring stanu systemu**

  **Typ**: Łatwość utrzymania | **Priorytet**: Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System powinien umożliwiać łatwe monitorowanie stanu, dostępności i szybkie diagnozowanie awarii.

  **Metryka**:  
   Średni czas potrzebny na identyfikację problemu od momentu jego wystąpienia oraz dostępność narzędzi diagnostycznych.

  **Sposób pomiaru**:  
   Pomiar czasu identyfikacji awarii podczas symulacji zdarzeń awaryjnych, weryfikacja dostępności narzędzi diagnostycznych 24/7.

  **Możliwe wyniki pomiaru**:  
   Czas diagnozy awarii (w minutach), dostępność narzędzi diagnostycznych (TAK/NIE).

  **Akceptowalne wartości pomiaru**:  
   Identyfikacja awarii poniżej 15 minut, narzędzia diagnostyczne dostępne 24/7.

- **(CJM0003) Łatwa testowalność**

  **Typ**: Łatwość utrzymania | **Priorytet**: Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System musi być zaprojektowany tak, by umożliwiać skuteczne przeprowadzanie testów automatycznych i manualnych.

  **Metryka**:  
   Procent pokrycia kodu testami automatycznymi, czas wykonania pełnej serii testów automatycznych.

  **Sposób pomiaru**:  
   Analiza pokrycia kodu narzędziami automatycznym, pomiar czasu wykonania całego zestawu testów automatycznych.

  **Możliwe wyniki pomiaru**:  
   Pokrycie kodu (%), czas wykonania pełnego zestawu testów (w minutach).

  **Akceptowalne wartości pomiaru**:  
   Pokrycie kodu co najmniej 80%, czas wykonania pełnej serii testów poniżej 60 minut.

- **(CJP0001) Aplikacja webowa i mobilna**

  **Typ**: Przenośność | **Priorytet**: Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi być dostępny jako aplikacja webowa oraz aplikacja mobilna (Android, iOS), zapewniając co najmniej 80% funkcjonalności aplikacji webowej w aplikacji mobilnej.

  **Metryka**:  
   Procent pokrycia funkcjonalności aplikacji webowej przez aplikację mobilną oraz ocena aplikacji mobilnej w sklepach aplikacji.

  **Sposób pomiaru**:  
   Porównanie funkcjonalności aplikacji mobilnej względem aplikacji webowej oraz analiza średnich ocen użytkowników w Google Play i App Store.

  **Możliwe wyniki pomiaru**:  
   Pokrycie funkcjonalności (%), średnia ocena aplikacji mobilnej w sklepach (skala 1-5).

  **Akceptowalne wartości pomiaru**:  
   Co najmniej 80% funkcjonalności aplikacji webowej dostępne w aplikacji mobilnej, średnia ocena aplikacji minimum 4.0 w sklepach aplikacji.

- **(CJK0001) Kompatybilność z popularnymi przeglądarkami**

  **Typ**: Kompatybilność | **Priorytet**: Kluczowy | **Trudność**: Średnia

  **Opis**:  
   System musi być w pełni kompatybilny z najpopularniejszymi przeglądarkami internetowymi (Chrome, Firefox, Edge, Safari).

  **Metryka**:  
   Procent poprawnie wykonanych przypadków testowych kompatybilności w każdej przeglądarce.

  **Sposób pomiaru**:  
   Testy manualne oraz automatyczne w popularnych przeglądarkach, z wykorzystaniem narzędzi typu Selenium, Playwright.

  **Możliwe wyniki pomiaru**:  
   Procent zgodności dla każdej z wymienionych przeglądarek.

  **Akceptowalne wartości pomiaru**:  
   ≥ 95% poprawności dla każdej z wymienionych przeglądarek.

- **(CJN0003) Odporność na błędy użytkownika**

  **Typ**: Niezawodność | **Priorytet**: Niski | **Trudność**: Średnia

  **Opis**:  
   System powinien być odporny na typowe błędy użytkowników, minimalizując ryzyko awarii lub błędnych operacji.

  **Metryka**:  
   Liczba błędów krytycznych zgłoszonych podczas testów użytkowników.

  **Sposób pomiaru**:  
   Testy manualne oraz analiza zgłoszeń użytkowników podczas sesji testowych, ocena częstotliwości występowania błędów.

  **Możliwe wyniki pomiaru**:  
   Liczba błędów krytycznych na 100 wykonanych operacji użytkownika.

  **Akceptowalne wartości pomiaru**:  
   ≤ 2 błędy krytyczne na 100 operacji.

- **(CJB0003) Zgodność z wymaganiami RODO**

  **Typ**: Bezpieczeństwo | **Priorytet**: Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi spełniać wymagania dotyczące ochrony danych osobowych określone w RODO (GDPR).

  **Metryka**:  
   Procent zgodności z wymogami RODO po audycie prawnym i technicznym.

  **Sposób pomiaru**:  
   Audyt ekspercki zgodności prawnej i technicznej z RODO, analiza raportu zgodności.

  **Możliwe wyniki pomiaru**:  
   Procent spełnienia wymogów RODO, liczba wykrytych niezgodności.

  **Akceptowalne wartości pomiaru**:  
   100% spełnienie kluczowych wymagań RODO, brak niezgodności krytycznych.

- **(CJK0002) Kompatybilność z innymi systemami (integracja CKAN)**

  **Typ**: Kompatybilność | **Priorytet**: Kluczowy | **Trudność**: Wysoka

  **Opis**:  
   System musi zapewniać możliwość łatwej integracji z systemami zewnętrznymi, szczególnie z systemem CKAN, umożliwiając wymianę danych oraz ich metadanych.

  **Metryka**:  
   Liczba poprawnie zintegrowanych źródeł danych w ramach CKAN.

  **Sposób pomiaru**:  
   Testy integracyjne z wykorzystaniem API CKAN, weryfikacja zgodności formatów danych, walidacja metadanych.

  **Możliwe wyniki pomiaru**:  
   Liczba źródeł danych zintegrowanych bez błędów, procent poprawnej integracji.

  **Akceptowalne wartości pomiaru**:  
   ≥ 90% poprawnej integracji testowanych źródeł danych.

- **(CJP0002) Wsparcie wielojęzyczności**

  **Typ**: Przenośność | **Priorytet**: Średni | **Trudność**: Średnia

  **Opis**:  
   System powinien obsługiwać wiele wersji językowych interfejsu użytkownika oraz metadanych, umożliwiając dostęp dla użytkowników z różnych krajów.

  **Metryka**:  
   Liczba obsługiwanych języków.

  **Sposób pomiaru**:  
   Weryfikacja interfejsu i bazy metadanych.

  **Możliwe wyniki pomiaru**:  
   Liczba języków.

  **Akceptowalne wartości pomiaru**:  
   ≥3 języki.

- **(CJU0004) Łatwość nauki obsługi systemu**

  **Typ**: Użyteczność | **Priorytet**: Niski | **Trudność**: Średnia

  **Opis**:  
   System powinien być łatwy do opanowania przez nowych użytkowników, skracając czas potrzebny na rozpoczęcie korzystania z jego funkcji.

  **Metryka**:  
   Średni czas realizacji kluczowych zadań przez nowych użytkowników.

  **Sposób pomiaru**:  
   Pomiar czasu realizacji podczas testów użyteczności.

  **Możliwe wyniki pomiaru**:  
   Czas w minutach.

  **Akceptowalne wartości pomiaru**:  
   ≤30 minut.
