# Pytania do wywiadu

## Dane i ich struktura
#### 1. Zbiór danych 
#### 2. Metadane - Kornelia Kołodziejska
- Jakie konkretne kategorie metadanych będą obowiązkowe dla każdego udostępnianego zbioru danych (np. tytuł, opis, data publikacji, autor, słowa kluczowe)?
- W jaki sposób proces wprowadzania metadanych zostanie zorganizowany? Czy będzie to proces manualny, automatyczny, czy mieszany?
- Czy użytkownicy będą mieli dostęp do historii zmian metadanych dla poszczególnych zbiorów danych?
- W jaki sposób będzie zapewniana jakość i aktualność metadanych? Czy będą prowadzone jakieś procesy weryfikacji?
  
#### 3. Dystrybucja zbioru danych - Łukasz Gumienniczuk
- Jakie formaty danych są używane podczas dystrybucji? (Metody dostarczania danych)
- Jakie są wymagania dotyczące bezpieczeństwa podczas dystrybucji danych? (podpisy cyfrowe, historia wersji)
- Czy użytkownicy będą mogli pobierać tylko całe zbiory, czy także ich wybrane fragmenty?
- Czy powinno istnieć ograniczenie liczby pobrań w określonym czasie (rate limiting)?
- Czy istnieją limity dotyczące wielkości lub częstotliwości przesyłania danych?
- Czy użytkownicy powinni mieć możliwość pobrania danych w formie paczek ZIP?
- Czy w przypadku posiadania historii wersji, użytkownik jest w stanie pobrać starszą wersję udostępnionych danych
- 
#### 4.  Otwarte dane publiczne - Jakub Klenkiewicz
- Jakie wymagania prawne lub regulacje dotyczące otwartych danych publicznych należy uwzględnić przy publikacji zbiorów danych?
- Kto będzie odpowiedzialny za weryfikację kompletności i poprawności otwartych danych publicznych przed ich udostępnieniem?
- Czy system będzie prowadził rejestr aktualnie dostępnych otwartych danych publicznych oraz ich wersji?
- W jaki sposób będą określane zasady ponownego wykorzystywania opublikowanych otwartych danych publicznych (np. czy zostaną opracowane wewnętrzne regulaminy lub wzory umów)?
- Czy planowane jest udostępnianie mechanizmów umożliwiających automatyczne publikowanie lub aktualizowanie otwartych danych publicznych (np. poprzez integrację z systemami wewnętrznymi)?
- Czy użytkownicy będą mogli składać wnioski o publikację nowych zbiorów w trybie otwartym, a jeśli tak, w jaki sposób zostanie zorganizowany proces rozpatrywania tych wniosków (np. formularz online, weryfikacja przez dedykowany zespół)?
- 
#### 5.  Schemat danych - Michał Ciechan
- Jak ma wyglądać proces zatwierdzania nowych lub uaktualnionych schematów danych?
  - Kto ma ustalać schemat danych? Weryfikator czy dostawca danych?
  - Czy system ma walidować istniejący zbiór danych, czy tylko nowe dane? Co w przypadku niepomyślnej walidacji?
- Czy schemat danych ma być powiązany ze zbiorem danych czy dystrybucją? Czyli jeden schemat dla różnych formatów, czy jeden schemat dla jednego formatu danych?
- Czy istnieją obowiązujące przepisy lub standardy branżowe nakładające wymagania na schematy danych?
- Jakie elementy powinny być zawarte w schemacie danych (np. nazwy pól, typy danych, formaty, relacje)?

## Dostęp i zarządzanie danymi
#### 6. Interfejs API 
#### 7. Zarządzanie dostępem do API  - Bartłomiej Janota
- W jaki sposób system będzie umożliwiał zarządzanie dostępem do API dla użytkowników i aplikacji zewnętrznych? 
- Jakie role lub uprawnienia będą definiowane w systemie w kontekście korzystania z API?
- Czy system będzie wspierał różne metody uwierzytelniania i autoryzacji dostępu do API (np. klucze API, token OAuth 2.0 itp.)?
- Czy system będzie rejestrował i monitorował próby dostępu do API, w tym informacje o użytkowniku/aplikacji, czasie dostępu i wykorzystanych zasobach?
#### 8. Monitorowanie wykorzystania API 


### Prezentacja i interakcja z danymi
#### 9. Wizualizacja danych 
#### 10. Uwaga do zbioru danych - Mikołaj Tradecki
- Jakie konkretnie informacje powinny być zbierane od użytkownika w momencie zgłaszania uwagi do zbioru danych?
- W jaki sposób użytkownik będzie mógł zgłosić uwagę?
- Czy użytkownik powinien mieć możliwość śledzenia statusu zgłoszonej przez siebie uwagi?
- Kto będzie odpowiedzialny za analizę zgłoszeń użytkowników?
- Czy system powinien rejestrować historię wszystkich zgłoszeń?
- Czy użytkownicy powinni mieć możliwość przeglądania uwag zgłoszonych przez innych użytkowników do danego zbioru danych?
- Czy przewidywana jest możliwość wystawiania opinii o zbiorze danych powiązanych ze zgłoszoną uwagą?
- Czy zgłoszone uwagi powinny być w jakiś sposób powiązane z metadanymi zbioru danych?

    
## Subskrypcja i powiadomienia
#### 11. Subskrypcja zbioru danych - Michał Jagodziński
- Czy użytkownicy będą mogli wybierać konkretne typy zmian w danych, o których chcą otrzymywać powiadomienia (np. tylko aktualizacje, zmiany w metadanych, nowe dane)? 
- Jakie informacje będą zawarte w powiadomieniach o zmianach zbiorów danych?
- Czy użytkownicy będą mogli subskrybować powiadomienia dla wielu zbiorów danych jednocześnie?
- W jaki sposób będzie wyglądać proces rejestracji do subskrypcji powiadomień? Czy będzie on wymagał logowania się, czy może użytkownicy będą mogli korzystać z funkcji anonimowo?
- Czy subskrybenci będą mogli dostosować częstotliwość otrzymywania powiadomień (np. natychmiastowo, codziennie, co tydzień)?
- Czy subskrybcja będzie płatna?
#### 12. Kanał powiadomień - Mateusz Borka
 - Jakie kanały powiadomień będą dostępne dla użytkowników (e-mail, SMS, powiadomienia push, komunikaty w systemie)?
 - Czy użytkownicy będą mogli konfigurować preferencje dotyczące powiadomień (częstotliwość, rodzaj informacji)?
 - W jakich sytuacjach system będzie wysyłał automatyczne powiadomienia (aktualizacja danych, błędy systemowe, zmiany w dostępie do API)?
 - Jak będzie zapewniona zgodność z RODO w kontekście przesyłania powiadomień (zgody użytkowników, prawo do rezygnacji)?Jak będzie zapewniona zgodność z RODO w kontekście przesyłania powiadomień (zgody użytkowników, prawo do rezygnacji)?

## Bezpieczeństwo i zgodność z regulacjami
#### 13. Zgodność z RODO - Michał Bibrzycki
- Jakie kategorie danych osobowych będą przetwarzane przez system?
- Jaka będzie podstawa prawna przetwarzania poszczególnych kategorii danych osobowych zgodnie z RODO (np. zgoda, wykonanie umowy, obowiązek prawny, uzasadniony interes administratora)?
- W jaki sposób system będzie umożliwiał realizację praw osób, których dane dotyczą, np:
    - prawo dostępu do danych
    - prawo do sprostowania
    - prawo do usunięcia danych
    - prawo do wniesienia sprzeciwu
- W jaki sposób system będzie zapewniał bezpieczeństwo przetwarzanych danych osobowych zgodnie z wymogami RODO?
- Jakie procedury zostaną wdrożone w systemie na wypadek naruszenia ochrony danych osobowych (data breach)?
- Czy system będzie wymagał zgody użytkowników na przetwarzanie danych osobowych w określonych celach? Jeśli tak, w jaki sposób zgoda będzie zbierana, dokumentowana i zarządzana (w tym możliwość jej wycofania)?
- Jakie mechanizmy kontroli dostępu zostaną zaimplementowane, aby zapewnić, że tylko upoważnione osoby mają dostęp do danych osobowych?
#### 14. Kopia zapasowa danych - Maciej Rukat
- Jak często powinna być tworzona kopia zapasowa danych?
- Jakie dane powinny być uwzględniane w kopii zapasowej? 
- W jakich lokalizacjach powinny być przechowywane kopie zapasowe?
- Jak długo powinny być przechowywane kopie zapasowe przed ich usunięciem?
- Kto powinien mieć dostęp do kopii zapasowych i możliwość ich przywracania?

## Użytkownicy i dostęp do systemu
#### 15.  Użytkownik systemu 
#### 16.  Logowanie do systemu - Mikołaj Frączek
- Jakie metody uwierzytelniania będą dostępne w systemie (np. login i hasło, 2FA, biometria, klucze sprzętowe)?
- Czy system będzie wspierał uwierzytelnianie wieloskładnikowe (MFA)? Jeśli tak, jakie metody MFA będą dostępne?
- Czy system będzie umożliwiał logowanie przy użyciu zewnętrznych dostawców tożsamości (np. Google, Microsoft, SSO)?
- Jakie polityki dotyczące haseł zostaną wdrożone (np. minimalna długość, złożoność, czas ważności)?
- Jakie mechanizmy zabezpieczeń będą stosowane w celu wykrywania i blokowania nieautoryzowanych prób logowania (np. blokada konta po określonej liczbie nieudanych prób)

## Audyt i zgodność operacyjna - Daria Koval
- Jakie mechanizmy audytu zostaną wdrożone w celu monitorowania operacji na danych?
- Czy system będzie przechowywał historię zmian danych i operacji użytkowników?
- Jakie procedury zostaną zastosowane do wykrywania i zgłaszania naruszeń polityki bezpieczeństwa?
- Czy przewidziane są okresowe przeglądy zgodności operacyjnej systemu z regulacjami prawnymi i standardami branżowymi?
- Jakie raporty dotyczące audytu będą generowane i kto będzie miał do nich dostęp?
- Czy system będzie obsługiwał mechanizmy automatycznego wykrywania anomalii w operacjach użytkowników?
