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
#### 4.  Otwarte dane publiczne 
#### 5.  Schemat danych - Michał Ciechan
- Jak ma wyglądać proces zatwierdzania nowych lub uaktualnionych schematów danych?
  - Kto ma ustalać schemat danych? Weryfikator czy dostawca danych?
  - Czy system ma walidować istniejący zbiór danych, czy tylko nowe dane? Co w przypadku niepomyślnej walidacji?
- Czy schemat danych ma być powiązany ze zbiorem danych czy dystrybucją? Czyli jeden schemat dla różnych formatów, czy jeden schemat dla jednego formatu danych?
- Czy istnieją obowiązujące przepisy lub standardy branżowe nakładające wymagania na schematy danych?
- Jakie elementy powinny być zawarte w schemacie danych (np. nazwy pól, typy danych, formaty, relacje)?

## Dostęp i zarządzanie danymi
#### 6. Interfejs API 
#### 7. Zarządzanie dostępem do API 
#### 8. Monitorowanie wykorzystania API 

## Prezentacja i interakcja z danymi
#### 9. Wizualizacja danych 
#### 10. Uwaga do zbioru danych
    
## Subskrypcja i powiadomienia
#### 11. Subskrypcja zbioru danych - Michał Jagodziński
- Czy użytkownicy będą mogli wybierać konkretne typy zmian w danych, o których chcą otrzymywać powiadomienia (np. tylko aktualizacje, zmiany w metadanych, nowe dane)? 
- Jakie informacje będą zawarte w powiadomieniach o zmianach zbiorów danych?
- Czy użytkownicy będą mogli subskrybować powiadomienia dla wielu zbiorów danych jednocześnie?
- W jaki sposób będzie wyglądać proces rejestracji do subskrypcji powiadomień? Czy będzie on wymagał logowania się, czy może użytkownicy będą mogli korzystać z funkcji anonimowo?
- Czy subskrybenci będą mogli dostosować częstotliwość otrzymywania powiadomień (np. natychmiastowo, codziennie, co tydzień)?
- Czy subskrybcja będzie płatna?
#### 12. Kanał powiadomień 

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
#### 16.  Logowanie do systemu 
